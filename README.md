# What is it?
This repository includes the sources and build/packaging scripts for isisisreleadyet.com - a fun project that shows how many bugs have to be fixed until the beta1 of Isis, the new Version of [elementary os](elementaryos.org) will be made available. Is Isis Released Yet makes use of [HLTI.py from Gabriel Perren](https://github.com/Gabriel-p/launchpad-bug-countdown). 

# Dependencies
* [invoke](https://github.com/pyinvoke/invoke)
* [fpm](https://github.com/jordansissel/fpm/wiki)
* [PyYAML](http://pyyaml.org/)
* [sh](https://github.com/amoffat/sh)

# Building the deb file
1) `cd _bnd`   
2) `invoke build_deb --config configs/isisisreleasedyet.com.yaml`  

The build script then creates the Debian package with configs and scritps needed to directly fire up Is Isis Relased Yet. I assume you are using Nginx and you'd like to store your mutable data in `/home/web/…`. All the immutable data are installed to `/srv/http/…`. You'll have to at least change the domain in the YAML config. Have fun tweaking it! :)

# Installation
Since this package comes with an Nginx config, cron-job and some scripts everything is up and running after a simple `dpkg -i isisisreleasedyet-com_0.20140615~094411_all.deb` – or, if you have your own debian repository, `apt-get install isisisreleasedyet-com`.

You can easily adopt this to other packaging systems and web servers. fpm also supports e.g. RPM.

# Authors

* HLTI.py: Gabriel Perren [GitHub](https://github.com/Gabriel-p)
* Design: Henrik Weber <weber@dajool.com>
* Deployment, HTML and glue code: Jochen Breuer <breuer@dajool.com>
