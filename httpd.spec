%define contentdir /var/www
%define suexec_caller apache
%define mmn 20020628

Summary: Apache HTTP Server
Name: httpd
Version: 2.0.40
Release: 11.7
URL: http://httpd.apache.org/
Source0: http://www.apache.org/dist/httpd/httpd-%{version}.tar.gz
Source1: index.html
Source3: httpd.logrotate
Source4: httpd.init
Source5: README.confd
Source6: powered_by.gif
Source10: httpd.conf
Source11: ssl.conf
Source12: migration.html
Source13: migration.css
Source14: mod_ssl-Makefile.crt
Source14: mod_ssl-Makefile.crl
# build/scripts patches
Patch1: httpd-2.0.40-apctl.patch
Patch2: httpd-2.0.36-apxs.patch
Patch3: httpd-2.0.36-sslink.patch
# Bug fixes
Patch20: httpd-2.0.40-davsegv.patch
Patch21: httpd-2.0.40-leaks.patch
Patch22: httpd-2.0.40-nphcgi.patch
Patch23: httpd-2.0.40-proxy.patch
Patch24: httpd-2.0.40-range.patch
Patch26: httpd-2.0.40-pipelog.patch
Patch27: httpd-2.0.40-rwmap.patch
Patch28: httpd-2.0.40-stream.patch
Patch29: httpd-2.0.40-subreq.patch
Patch30: httpd-2.0.40-sslexcl.patch
Patch31: httpd-2.0.40-include.patch
# features/functional changes
Patch40: httpd-2.0.36-cnfdir.patch
Patch41: httpd-2.0.36-redhat.patch
Patch42: httpd-2.0.40-xfsz.patch
Patch43: httpd-2.0.40-pod.patch
Patch44: httpd-2.0.40-prctl.patch
# Security fixes
Patch60: httpd-2.0.40-CAN-2002-0840.patch
Patch61: httpd-2.0.40-CAN-2002-0843.patch
Patch62: httpd-2.0.40-CAN-2003-0132.patch
Patch63: httpd-2.0.40-CAN-2003-0020.patch
Patch64: httpd-2.0.40-fdleak.patch
Patch65: httpd-2.0.40-CAN-2003-0083.patch
Patch66: httpd-2.0.40-CAN-2003-0245.patch
Patch68: httpd-2.0.40-CAN-2003-0192.patch
Patch69: httpd-2.0.40-CAN-2003-0253.patch
Patch70: httpd-2.0.40-CAN-2003-0254.patch
Patch71: httpd-2.0.40-VU379828.patch
License: Apache Software License
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-root
BuildPrereq: db4-devel, expat-devel, findutils, perl
Requires: /etc/mime.types, gawk, /usr/share/magic.mime, /usr/bin/find
Prereq: /sbin/chkconfig, /bin/mktemp, /bin/rm, /bin/mv
Prereq: sh-utils, textutils, /usr/sbin/useradd
Provides: webserver
Provides: httpd-mmn = %{mmn}
Conflicts: thttpd
Obsoletes: apache, secureweb, mod_dav

%description
Apache is a powerful, full-featured, efficient, and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%package devel
Group: Development/Libraries
Summary: Development tools for the Apache HTTP server.
Obsoletes: secureweb-devel, apache-devel
Requires: libtool, httpd = %{version}

%description devel
The httpd-devel package contains the APXS binary and other files
that you need to build Dynamic Shared Objects (DSOs) for Apache.

If you are installing the Apache HTTP server and you want to be
able to compile or develop additional modules for Apache, you need
to install this package.

%package manual
Group: Documentation
Summary: Documentation for the Apache HTTP server.
Obsoletes: secureweb-manual, apache-manual

%description manual
The httpd-manual package contains the complete manual and
reference guide for the Apache HTTP server. The information can
also be found at http://httpd.apache.org/docs/.

%package -n mod_ssl
Group: System Environment/Daemons
Summary: SSL/TLS module for the Apache HTTP server
Serial: 1
BuildPrereq: openssl-devel
Prereq: openssl, dev, /bin/cat
Requires: httpd, make, httpd-mmn = %{mmn}

%description -n mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer
Security (TLS) protocols.

%prep
%setup -q
%patch1 -p0 -b .apctl
%patch2 -p1 -b .apxs
%patch3 -p0 -b .sslink

%patch20 -p1 -b .davsegv
%patch21 -p0 -b .leaks
%patch22 -p1 -b .nphcgi
%patch23 -p1 -b .proxy
%patch24 -p1 -b .range
%patch26 -p1 -b .pipelog
%patch27 -p1 -b .rwmap
%patch28 -p1 -b .stream
%patch29 -p1 -b .subreq
%patch30 -p1 -b .sslexcl
%patch31 -p1 -b .include

%patch40 -p0 -b .cnfdir
%patch41 -p0 -b .redhat
%patch42 -p0 -b .xfsz
%patch43 -p0 -b .pod
%patch44 -p1 -b .prctl

%patch60 -p1 -b .can0840
%patch61 -p1 -b .can0843
%patch62 -p1 -b .can0132
%patch63 -p1 -b .can0020
%patch64 -p1 -b .fdleak
%patch65 -p1 -b .can0083
%patch66 -p1 -b .can0245
%patch68 -p1 -b .can0192
%patch69 -p1 -b .can0253
%patch70 -p1 -b .can0254
%patch71 -p1 -b .vu379828

# copy across the migration guide and sed it's location into apachectl
cp $RPM_SOURCE_DIR/migration.{html,css} .

# regenerate configure scripts
./buildconf

%build
# Fix version in apachectl
%{__perl} -pi -e "s:\@docdir\@:%{_docdir}/%{name}-%{version}:g" \
	support/apachectl.in

CFLAGS="$RPM_OPT_FLAGS" \
AP_LIBS="-lssl -lcrypto" \
./configure \
 	--prefix=%{_sysconfdir}/httpd \
 	--exec-prefix=%{_prefix} \
 	--bindir=%{_bindir} \
 	--sbindir=%{_sbindir} \
 	--mandir=%{_mandir} \
	--sysconfdir=%{_sysconfdir}/httpd/conf \
	--includedir=%{_includedir}/httpd \
	--libexecdir=%{_libdir}/httpd/modules \
	--datadir=%{contentdir} \
	--with-mpm=prefork \
	--enable-mods-shared=all \
	--enable-suexec --with-suexec \
	--with-suexec-caller=%{suexec_caller} \
	--with-suexec-docroot=%{contentdir} \
	--with-suexec-logfile=%{_localstatedir}/log/httpd/suexec.log \
	--with-suexec-bin=%{_sbindir}/suexec \
	--with-suexec-uidmin=500 --with-suexec-gidmin=500 \
	--enable-ssl --with-ssl \
	--enable-deflate \
	--enable-proxy --enable-proxy-connect \
	--enable-proxy-http --enable-proxy-ftp
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# Classify ab and logresolve as section 1 commands, as they are in /usr/bin
mv docs/man/ab.8 docs/man/ab.1
sed -e "1s/logresolve 8/logresolve 1/" \
  < docs/man/logresolve.8 > docs/man/logresolve.1
rm docs/man/logresolve.8

make DESTDIR=$RPM_BUILD_ROOT install

### remove this
# strip -g $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.so

# install conf file/directory
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/README.confd \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/README
install -m 644 $RPM_SOURCE_DIR/ssl.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/ssl.conf

rm $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/*.conf
install -m 644 $RPM_SOURCE_DIR/httpd.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/httpd.conf

# mod_ssl bits
for suffix in crl crt csr key prm; do
   mkdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/ssl.${suffix}
done

# Makefiles for certificate management
for ext in crt crl; do 
  install -m 644 $RPM_SOURCE_DIR/mod_ssl-Makefile.${ext} \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/ssl.${ext}/Makefile.${ext}
done
ln -s ../../../usr/share/ssl/certs/Makefile $RPM_BUILD_ROOT/etc/httpd/conf

# for holding mod_dav lock database
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/dav

# create a prototype session cache
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/mod_ssl
touch $RPM_BUILD_ROOT%{_localstatedir}/cache/mod_ssl/scache.{dir,pag,sem}

# move utilities to /usr/bin
mv $RPM_BUILD_ROOT%{_sbindir}/{ab,htdbm,logresolve,htpasswd,htdigest} \
   $RPM_BUILD_ROOT%{_bindir}

# make libtool a symlink
mv $RPM_BUILD_ROOT%{contentdir}/build $RPM_BUILD_ROOT%{_libdir}/httpd/build
rm $RPM_BUILD_ROOT%{_libdir}/httpd/build/libtool
ln -s ../../../..%{_bindir}/libtool $RPM_BUILD_ROOT%{_libdir}/httpd/build/libtool

# fix up config_vars file: relocate the build directory into libdir;
# reference correct libtool; remove references to RPM build root.
sed -e "s|%{contentdir}/build|%{_libdir}/httpd/build|g" \
    -e "/AP_LIBS/d" -e "/abs_srcdir/d" \
    -e "/^LIBTOOL/s|/[^ ]*/libtool|%{_bindir}/libtool|" \
    -e "s|^EXTRA_INCLUDES.*$|EXTRA_INCLUDES = -I\$(includedir) -I%{_includedir}/openssl|g" \
  < build/config_vars.mk \
  > $RPM_BUILD_ROOT%{_libdir}/httpd/build/config_vars.mk
install -m 644 build/special.mk \
    $RPM_BUILD_ROOT%{_libdir}/httpd/build/special.mk

# Make the MMN accessible to module packages
echo %{mmn} > $RPM_BUILD_ROOT%{_includedir}/httpd/.mmn

# docroot
mkdir $RPM_BUILD_ROOT%{contentdir}/html
install -m 644 $RPM_SOURCE_DIR/index.html \
	$RPM_BUILD_ROOT%{contentdir}/error/noindex.html
rm -r $RPM_BUILD_ROOT%{contentdir}/manual/style
rm $RPM_BUILD_ROOT%{contentdir}/manual/*/*.xml

install -m 644 $RPM_SOURCE_DIR/powered_by.gif \
	$RPM_BUILD_ROOT%{contentdir}/icons

# logs
rmdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/logs
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/httpd

# symlinks for /etc/httpd
ln -s ../..%{_localstatedir}/log/httpd $RPM_BUILD_ROOT/etc/httpd/logs
ln -s ../..%{_localstatedir}/run $RPM_BUILD_ROOT/etc/httpd/run
ln -s ../..%{_libdir}/httpd/modules $RPM_BUILD_ROOT/etc/httpd/modules
ln -s ../..%{_libdir}/httpd/build $RPM_BUILD_ROOT/etc/httpd/build

# install SYSV init stuff
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m755 $RPM_SOURCE_DIR/httpd.init \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
%{__perl} -pi -e "s:\@docdir\@:%{_docdir}/%{name}-%{version}:g" \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/httpd	

# install log rotation stuff
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m644 $RPM_SOURCE_DIR/httpd.logrotate \
	$RPM_BUILD_ROOT/etc/logrotate.d/httpd

# fix man page paths
sed -e "s|/usr/local/apache2/conf/httpd.conf|/etc/httpd/conf/httpd.conf|" \
    -e "s|/usr/local/apache2/conf/mime.types|/etc/mime.types|" \
    -e "s|/usr/local/apache2/conf/magic|/etc/httpd/conf/magic|" \
    -e "s|/usr/local/apache2/logs/error_log|/var/log/httpd/error_log|" \
    -e "s|/usr/local/apache2/logs/access_log|/var/log/httpd/access_log|" \
    -e "s|/usr/local/apache2/logs/httpd.pid|/var/run/httpd.pid|" \
    -e "s|/usr/local/apache2|/etc/httpd|" < docs/man/httpd.8 \
  > $RPM_BUILD_ROOT%{_mandir}/man8/httpd.8

%pre
# Add the "apache" user
/usr/sbin/useradd -c "Apache" -u 48 \
	-s /sbin/nologin -r -d %{contentdir} apache 2> /dev/null || :

%triggerpostun -- apache < 2.0
/sbin/chkconfig --add httpd

%post
# Register the httpd service
/sbin/chkconfig --add httpd

%preun
if [ $1 = 0 ]; then
	/sbin/service httpd stop > /dev/null 2>&1
	/sbin/chkconfig --del httpd
fi

%post -n mod_ssl
/sbin/ldconfig ### is this needed?
umask 077

if [ ! -f %{_sysconfdir}/httpd/conf/ssl.key/server.key ] ; then
%{_bindir}/openssl genrsa -rand /proc/apm:/proc/cpuinfo:/proc/dma:/proc/filesystems:/proc/interrupts:/proc/ioports:/proc/pci:/proc/rtc:/proc/uptime 1024 > %{_sysconfdir}/httpd/conf/ssl.key/server.key 2> /dev/null
fi

FQDN=`hostname`
if [ "x${FQDN}" = "x" ]; then
   FQDN=localhost.localdomain
fi

if [ ! -f %{_sysconfdir}/httpd/conf/ssl.crt/server.crt ] ; then
cat << EOF | %{_bindir}/openssl req -new -key %{_sysconfdir}/httpd/conf/ssl.key/server.key -x509 -days 365 -out %{_sysconfdir}/httpd/conf/ssl.crt/server.crt 2>/dev/null
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
${FQDN}
root@${FQDN}
EOF
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%doc ABOUT_APACHE README CHANGES ROADMAP LICENSE
%doc migration.html migration.css

%dir %{_sysconfdir}/httpd
%{_sysconfdir}/httpd/modules
%{_sysconfdir}/httpd/logs
%{_sysconfdir}/httpd/run
%dir %{_sysconfdir}/httpd/conf
%config(noreplace) %{_sysconfdir}/httpd/conf/*.conf
%config(noreplace) %{_sysconfdir}/httpd/conf/magic

%config %{_sysconfdir}/logrotate.d/httpd
%config %{_sysconfdir}/rc.d/init.d/httpd

%dir %{_sysconfdir}/httpd/conf.d
%{_sysconfdir}/httpd/conf.d/README

%{_bindir}/ab
%{_bindir}/ht*
%{_bindir}/logresolve
%{_sbindir}/httpd
%{_sbindir}/apachectl
%{_sbindir}/rotatelogs
%attr(4510,root,%{suexec_caller}) %{_sbindir}/suexec

%{_libdir}/libapr.so.*
%{_libdir}/libaprutil.so.*

%dir %{_libdir}/httpd
%dir %{_libdir}/httpd/modules
# everything but mod_ssl.so:
%{_libdir}/httpd/modules/mod_[a-r]*.so
%{_libdir}/httpd/modules/mod_s[petu]*.so
%{_libdir}/httpd/modules/mod_[t-z]*.so

%dir %{contentdir}
%dir %{contentdir}/cgi-bin
%dir %{contentdir}/html
%dir %{contentdir}/icons
%dir %{contentdir}/error
%dir %{contentdir}/error/include
%{contentdir}/icons/*
%{contentdir}/error/README
%{contentdir}/error/noindex.html
%config(noreplace) %{contentdir}/error/*.var
%config(noreplace) %{contentdir}/error/include/*.html

%attr(0700,root,root) %dir %{_localstatedir}/log/httpd

%attr(0700,apache,apache) %dir %{_localstatedir}/lib/dav

%{_mandir}/man1/*

%{_mandir}/man8/apachectl*
%{_mandir}/man8/httpd*
%{_mandir}/man8/rotatelogs*
%{_mandir}/man8/suexec*

%files manual
%defattr(-,root,root)
%{contentdir}/manual

%files -n mod_ssl
%defattr(-,root,root)
%{_libdir}/httpd/modules/mod_ssl.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/ssl.conf
%attr(0700,root,root) %dir %{_sysconfdir}/httpd/conf/ssl.*
%config %{_sysconfdir}/httpd/conf/Makefile
%config %{_sysconfdir}/httpd/conf/ssl.*/*
%attr(0700,apache,root) %dir %{_localstatedir}/cache/mod_ssl
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.dir
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.pag
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.sem

%files devel
%defattr(-,root,root)
%{_libdir}/libapr.so
%{_libdir}/libaprutil.so
%{_includedir}/httpd
%{_sysconfdir}/httpd/build
%{_sbindir}/apxs
%{_mandir}/man8/apxs.8*
%dir %{_libdir}/httpd/build
%{_libdir}/httpd/build/*.mk
%{_libdir}/httpd/build/instdso.sh
%{_libdir}/httpd/build/libtool

%changelog
* Wed Jul  9 2003 Joe Orton <jorton@redhat.com> 2.0.40-11.7
- add security fixes for CVE CAN-2003-0192, CAN-2003-0253, 
  CAN-2003-0254, CERT VU#379828
- add bug fixes for #78019, #82985, #85022, #97111, #98545, #98653
- install special.mk, fix apxs -q LIBTOOL (#92313)
- add mod_include fixes from upstream

* Tue May 27 2003 Joe Orton <jorton@redhat.com> 2.0.40-11.6
- add mod_ssl renegotiation fix

* Thu May 22 2003 Joe Orton <jorton@redhat.com> 2.0.40-11.5
- rebuild

* Mon May 12 2003 Joe Orton <jorton@redhat.com> 2.0.40-11.4
- add security fix for CAN-2003-0245
- add bug fixes for #89179, #88575, #89086

* Tue Apr  1 2003 Joe Orton <jorton@redhat.com> 2.0.40-11.3
- add security fixes for CAN-2003-0020, CAN-2003-0132, CAN-2003-0083
- add security fix for file descriptor leaks, #82142
- add bug fixes for #73428, #82587, #86254

* Wed Oct  9 2002 Joe Orton <jorton@redhat.com> 2.0.40-11
- correct SERVER_NAME encoding in i18n error pages (thanks to Andre Malo)

* Wed Oct  9 2002 Joe Orton <jorton@redhat.com> 2.0.40-10
- fix patch for CAN-2002-0840 to also cover i18n error pages

* Wed Oct  2 2002 Joe Orton <jorton@redhat.com> 2.0.40-9
- security fixes for CAN-2002-0840 and CAN-2002-0843
- fix for possible mod_dav segfault for certain requests

* Tue Sep 24 2002 Gary Benson <gbenson@redhat.com>
- updates to the migration guide

* Wed Sep  4 2002 Nalin Dahyabhai <nalin@redhat.com> 2.0.40-8
- link httpd with libssl to avoid library loading/unloading weirdness

* Tue Sep  3 2002 Joe Orton <jorton@redhat.com> 2.0.40-7
- add LoadModule lines for proxy modules in httpd.conf (#73349)
- fix permissions of conf/ssl.*/ directories; add Makefiles for
  certificate management (#73352)

* Mon Sep  2 2002 Joe Orton <jorton@redhat.com> 2.0.40-6
- provide "httpd-mmn" to manage module ABI compatibility

* Sun Sep  1 2002 Joe Orton <jorton@redhat.com> 2.0.40-5
- fix SSL session cache (#69699)
- revert addition of LDAP support to apr-util

* Mon Aug 26 2002 Joe Orton <jorton@redhat.com> 2.0.40-4
- set SIGXFSZ disposition to "ignored" (#69520)
- make dummy connections to the first listener in config (#72692)

* Mon Aug 26 2002 Joe Orton <jorton@redhat.com> 2.0.40-3
- allow "apachectl configtest" on a 1.3 httpd.conf
- add mod_deflate
- enable LDAP support in apr-util
- don't package everything in /var/www/error as config(noreplace)

* Wed Aug 21 2002 Bill Nottingham <notting@redhat.com> 2.0.40-2
- add trigger (#68657)

* Mon Aug 12 2002 Joe Orton <jorton@redhat.com> 2.0.40-1
- update to 2.0.40

* Wed Jul 24 2002 Joe Orton <jorton@redhat.com> 2.0.36-8
- improve comment on use of UserDir in default config (#66886)

* Wed Jul 10 2002 Joe Orton <jorton@redhat.com> 2.0.36-7
- use /sbin/nologin as shell for apache user (#68371)
- add patch from CVS to fix possible infinite loop when processing
  internal redirects

* Wed Jun 26 2002 Gary Benson <gbenson@redhat.com> 2.0.36-6
- modify init script to detect 1.3.x httpd.conf's and direct users
  to the migration guide

* Tue Jun 25 2002 Gary Benson <gbenson@redhat.com> 2.0.36-5
- patch apachectl to detect 1.3.x httpd.conf's and direct users
  to the migration guide
- ship the migration guide

* Fri Jun 21 2002 Joe Orton <jorton@redhat.com>
- move /etc/httpd2 back to /etc/httpd
- add noindex.html page and poweredby logo; tweak default config
  to load noindex.html if no default "/" page is present.
- add patch to prevent mutex errors on graceful restart

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 2.0.36-4
- automated rebuild

* Wed Jun 12 2002 Joe Orton <jorton@redhat.com> 2.0.36-3
- add patch to fix SSL mutex handling

* Wed Jun 12 2002 Joe Orton <jorton@redhat.com> 2.0.36-2
- improved config directory patch

* Mon May 20 2002 Joe Orton <jorton@redhat.com>
- initial build; based heavily on apache.spec and mod_ssl.spec
- fixes: #65214, #58490, #57376, #61265, #65518, #58177, #57245
