# What is it?
This repository includes the sources and build/packaging scripts for isfreyareleadyet.com - a fun project that shows how many bugs have to be fixed until the beta 1 of Freys, the new Version of [elementary os](http://elementaryos.org) will be made available. Is Freya Released Yet makes use of [HLTI.py from Gabriel Perren](https://github.com/Gabriel-p/launchpad-bug-countdown).

## UPDATE:
The [Beta 1](http://elementaryos.org/journal/freya-beta-1-available-for-developers-testers) has been released and looks really awesome. IFRY is no longer needed, but I'd like to publish some number here: 99,783 unique visitors with 581,546 total requests in roughly two month. Nearly 9,700 visitors a day. Most of the visitors already run Linux (52,336), but 19,408 visitors used Windows. I guess the 20,393 visitors with _Unknown_ Operating Systems are using iOS or Android.  
Most people visited IFRY directly. G+ brought 11,847 visitors and vk.com (don't know what it is) 7,436. Interestingly reddit and fuckyeah-elementaryos.tumblr.com are nearly on par with 5,592 and 4,333 visitors.  
And a whole bunch of people googled for the URL. ;)

![Server Log](https://bytebucket.org/brejoc/isisisreleasedyet.com/raw/b4637fd0f433ac050a0c1e63252a7f5b2011bc26/doc/server_log.png)

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
* davidak [GitHub](https://github.com/davidak) [Website](http://davidak.de/)
