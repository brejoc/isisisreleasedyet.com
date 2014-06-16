# -*- coding: utf-8 -*-

import os
import sys
import yaml
from invoke import run, task
from tasks_helper import *

@task()
def clean(*args, **kwargs):
    """\
    Remove all build files, configs and packages."
    """
    run("rm -rf ./build")
    run("rm -rf ./build_configs")
    run("rm -f *.deb")


@task("clean", "prepare_paths", "config_nginx", "config_post_install", "config_pre_uninstall")
def build_deb(config):
    """\
    Prepares the build and generates the package.
    """
    # get values from config
    stream = file(config, 'r')
    config_values = yaml.load(stream)

    base_path = config_values['build-vars']['srv_path'] + config_values['build-vars']['domain']
    
    # copy configs
    run("cp ./build_configs/%s ./build/etc/nginx/sites-available/." % (config_values['build-vars']['domain'], ))
    run("echo '#!/bin/sh\n\n/usr/bin/hlti 1> /home/web/%(domain)s/cache/index.html.new && cp /home/web/%(domain)s/cache/index.html.new /home/web/%(domain)s/cache/index.html' > ./build/etc/cron.hourly/hlti" % {"domain": config_values['build-vars']['domain']})
    run("chmod +x ./build/etc/cron.hourly/hlti")

    run("ln -s /home/web/%s/cache/index.html ./build%s/index.html" % (config_values['build-vars']['domain'], os.path.join(base_path, "htdocs")))
    run("cp -R ../isisisreleasedyet/static ./build%s" % (os.path.join(base_path, "htdocs")))
    run("cp -R ../isisisreleasedyet/jinja_templates ./build%s" % (os.path.join(base_path, "lib")))

    run("cp ../isisisreleasedyet/hlti ./build/usr/bin/.")
    
    # generate version number
    version = "%(major)s.%(minor)s" % \
        {
            'major': get_major_version(), 
            'minor': get_minor_version()
        }

    package(config, {'version': version})
    

@task()
def prepare_paths(config):
    """\
    Prepare folder structure.
    """
    
    # get values from config
    stream = file(config, 'r')
    config_values = yaml.load(stream)
    base_path = config_values['build-vars']['srv_path'] + \
        config_values['build-vars']['domain']
    
    # make directories
    for folder in ['lib', 'htdocs', 'auth']:
        mkdirp("./build" + os.path.join(base_path, folder))
    mkdirp("./build/etc/nginx/sites-available")
    mkdirp("./build/usr/bin/")
    mkdirp("./build/etc/cron.hourly/")
    mkdirp("./build_configs")


@task
def config_pre_uninstall(config):
    """\
    Generate pre uninstall script from template.
    """
    generate_config("pre_uninstall",
                    config,
                    os.path.join("build_configs", "pre_uninstall.sh"))


@task
def config_post_install(config):
    """\
    Generate post install script from template.
    """
    generate_config("post_install",
                    config,
                    os.path.join("build_configs", "post_install.sh"))


@task
def config_nginx(config=''):
    """\
    Generate nginx config from template.
    """
    stream = file(config, 'r')
    config_values = yaml.load(stream)
    generate_config("nginx_config",
                    config,
                    os.path.join("build_configs", config_values['build-vars']['domain']))
