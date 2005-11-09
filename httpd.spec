%define contentdir /var/www
%define suexec_caller apache
%define mmn 20020903
%define vstring Fedora
%define distro Fedora Core

Summary: Apache HTTP Server
Name: httpd
Version: 2.0.54
Release: 16
URL: http://httpd.apache.org/
Source0: http://www.apache.org/dist/httpd/httpd-%{version}.tar.gz
Source1: index.html
Source3: httpd.logrotate
Source4: httpd.init
Source5: httpd.sysconf
Source7: powered_by_fedora.png
Source10: httpd.conf
Source11: ssl.conf
Source12: welcome.conf
Source13: manual.conf
# Documentation
Source30: migration.xml
Source31: migration.css
Source32: html.xsl
Source33: README.confd
# build/scripts patches
Patch1: httpd-2.0.40-apctl.patch
Patch2: httpd-2.0.36-apxs.patch
Patch3: httpd-2.0.48-linkmods.patch
Patch4: httpd-2.0.45-deplibs.patch
Patch5: httpd-2.0.47-pie.patch
Patch6: httpd-2.0.45-syspcre.patch
Patch8: httpd-2.0.48-vpathinc.patch
Patch9: httpd-2.0.52-apctlopts.patch
# Bug fixes
Patch20: httpd-2.0.45-encode.patch
Patch21: httpd-2.0.45-davetag.patch
Patch22: httpd-2.0.47-ldapshm.patch
Patch23: httpd-2.0.48-vhost.patch
Patch24: httpd-2.0.46-sslmutex.patch
Patch25: httpd-2.0.46-md5dig.patch
Patch26: httpd-2.0.48-proxy11.patch
Patch27: httpd-2.0.48-sslpphrase.patch
Patch28: httpd-2.0.48-worker.patch
Patch29: httpd-2.0.48-workerhup.patch
Patch30: httpd-2.0.48-davmisc.patch
Patch31: httpd-2.0.54-ssltrans.patch
Patch32: httpd-2.0.54-userdir.patch
Patch33: httpd-2.0.54-ldapconn.patch
Patch34: httpd-2.0.52-pipedlog1.patch
Patch35: httpd-2.0.52-pipedlog2.patch
Patch36: httpd-2.0.52-sslbuff.patch
Patch37: httpd-2.0.54-include.patch
Patch38: httpd-2.0.54-digest.patch
Patch39: httpd-2.0.54-ldap.patch
Patch40: httpd-2.0.54-sslnbio.patch
Patch41: httpd-2.0.54-sslreneg.patch
# Features/functional changes
Patch70: httpd-2.0.48-release.patch
Patch71: httpd-2.0.40-xfsz.patch
Patch72: httpd-2.0.40-pod.patch
Patch73: httpd-2.0.40-noshmht.patch
Patch74: httpd-2.0.45-export.patch
Patch75: httpd-2.0.48-dynlimit.patch
Patch76: httpd-2.0.48-dynamic.patch
Patch77: httpd-2.0.48-sslstatus.patch
Patch78: httpd-2.0.48-corelimit.patch
Patch80: httpd-2.0.48-distcache.patch
Patch81: httpd-2.0.48-debuglog.patch
Patch82: httpd-2.0.48-abench.patch
Patch84: httpd-2.0.48-sslheader.patch
Patch85: httpd-2.0.48-sslvars2.patch
Patch89: httpd-2.0.49-headerssl.patch
Patch90: httpd-2.0.49-workerstack.patch
Patch91: httpd-2.0.46-testhook.patch
Patch92: httpd-2.0.46-dumpcerts.patch
Patch93: httpd-2.0.54-selinux.patch
Patch94: httpd-2.0.54-openssl-098.patch
# Security fixes
Patch110: httpd-2.0.52-CAN-2005-1268.patch
Patch111: httpd-2.0.52-CAN-2005-2088.patch
Patch112: httpd-2.0.52-CAN-2005-2700.patch
Patch113: httpd-2.0.52-CAN-2005-2728.patch
License: Apache Software License
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: db4-devel, expat-devel, findutils, perl, pkgconfig, xmlto >= 0.0.11
BuildRequires: apr-devel >= 0.9.4-20, apr-util-devel, pcre-devel >= 5.0, 
BuildRequires: zlib-devel, libselinux-devel
Requires: /etc/mime.types, gawk, /usr/share/magic.mime, /usr/bin/find
Obsoletes: httpd-suexec
Prereq: /sbin/chkconfig, /bin/mktemp, /bin/rm, /bin/mv
Prereq: sh-utils, textutils, /usr/sbin/useradd
Provides: webserver
Provides: httpd-mmn = %{mmn}
Obsoletes: apache, secureweb, mod_dav, mod_gzip, stronghold-apache, stronghold-htdocs
Obsoletes: mod_put, mod_roaming
Conflicts: pcre < 4.0

%description
The Apache HTTP Server is a powerful, efficient, and extensible
web server.

%package devel
Group: Development/Libraries
Summary: Development tools for the Apache HTTP server.
Obsoletes: secureweb-devel, apache-devel, stronghold-apache-devel
Requires: apr-devel, apr-util-devel, pcre-devel >= 0:5.0
Requires: httpd = %{version}-%{release}

%description devel
The httpd-devel package contains the APXS binary and other files
that you need to build Dynamic Shared Objects (DSOs) for the
Apache HTTP Server.

If you are installing the Apache HTTP server and you want to be
able to compile or develop additional modules for Apache, you need
to install this package.

%package manual
Group: Documentation
Summary: Documentation for the Apache HTTP server.
Requires: httpd = %{version}-%{release}
Obsoletes: secureweb-manual, apache-manual

%description manual
The httpd-manual package contains the complete manual and
reference guide for the Apache HTTP server. The information can
also be found at http://httpd.apache.org/docs-2.0/.

%package -n mod_ssl
Group: System Environment/Daemons
Summary: SSL/TLS module for the Apache HTTP server
Epoch: 1
BuildRequires: openssl-devel, distcache-devel
Requires(post): openssl >= 0.9.7f-4, /bin/cat
Requires: httpd = 0:%{version}-%{release}, httpd-mmn = %{mmn}
Obsoletes: stronghold-mod_ssl

%description -n mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer
Security (TLS) protocols.

%prep
%setup -q
%patch1 -p1 -b .apctl
%patch2 -p1 -b .apxs
%patch3 -p1 -b .linkmods
%patch4 -p1 -b .deplibs
%patch5 -p1 -b .pie
%patch6 -p1 -b .syspcre
%patch8 -p1 -b .vpathinc
%patch9 -p1 -b .apctlopts

# no -b to prevent droplets in install root
%patch20 -p1
%patch21 -p1 -b .davetag
%patch22 -p1 -b .ldapshm
%patch23 -p1 -b .vhost
%patch24 -p1 -b .sslmutex
%patch25 -p1 -b .md5dig
%patch26 -p1 -b .proxy11
%patch27 -p1 -b .sslpphrase
%patch28 -p1 -b .worker
%patch29 -p1 -b .workerhup
%patch30 -p1 -b .davmisc
%patch31 -p1 -b .ssltrans
%patch32 -p1 -b .userdir
%patch33 -p1 -b .ldapconn
%patch34 -p1 -b .pipedlog1
%patch35 -p1 -b .pipedlog2
%patch36 -p1 -b .sslbuff
%patch37 -p1 -b .include
%patch38 -p1 -b .digest
%patch39 -p1 -b .ldap
%patch40 -p1 -b .sslnbio

%patch71 -p0 -b .xfsz
%patch72 -p1 -b .pod
%patch73 -p1 -b .noshmht
%patch74 -p1 -b .export
%patch75 -p1 -b .dynlimit
%patch76 -p1 -b .dynamic
%patch77 -p1 -b .sslstatus
%patch78 -p1 -b .corelimit
%patch80 -p1 -b .distcache
%patch81 -p1 -b .debuglog
%patch82 -p1 -b .abench
%patch84 -p1 -b .sslheader
%patch85 -p1 -b .sslvars2
%patch89 -p1 -b .headerssl
%patch90 -p1 -b .workerstack
%patch91 -p1 -b .testhook
%patch92 -p1 -b .dumpcerts
%patch93 -p1 -b .selinux
%patch94 -p1 -b .openssl-098

%patch41 -p1 -b .sslreneg

%patch110 -p1 -b .can1268
%patch111 -p1 -b .can2088
%patch112 -p1 -b .can2700
%patch113 -p1 -b .can2728

# Patch in vendor/release string
sed "s/@RELEASE@/%{vstring}/" < %{PATCH70} | patch -p1

# Safety check: prevent build if defined MMN does not equal upstream MMN.
vmmn=`echo MODULE_MAGIC_NUMBER_MAJOR | cpp -include include/ap_mmn.h | sed -n '/^2/p'`
if test "x${vmmn}" != "x%{mmn}"; then
   : Error: Upstream MMN is now ${vmmn}, packaged MMN is %{mmn}.
   : Update the mmn macro and rebuild.
   exit 1
fi

: Building for '%{distro}' with MMN %{mmn} and vendor string '%{vstring}'

%build
# forcibly prevent use of bundled apr, apr-util, pcre
rm -rf srclib/{apr,apr-util,pcre}
rm -f include/pcreposix.h

# regenerate configure scripts
autoheader && autoconf || exit 1

# Limit size of CHANGES to recent history
echo '1,/Changes with Apache MPM/wq' | ed CHANGES

# Before configure; fix location of build dir in generated apxs
%{__perl} -pi -e "s:\@exp_installbuilddir\@:%{_libdir}/httpd/build:g" \
	support/apxs.in
# update location of migration guide in apachectl
%{__perl} -pi -e "s:\@docdir\@:%{_docdir}/%{name}-%{version}:g" \
	support/apachectl.in

# Build the migration guide
sed 's/@DISTRO@/%{distro}/' < $RPM_SOURCE_DIR/migration.xml > migration.xml
xmlto -x $RPM_SOURCE_DIR/html.xsl html-nochunks migration.xml
cp $RPM_SOURCE_DIR/migration.css . # make %%doc happy

CFLAGS=$RPM_OPT_FLAGS
CPPFLAGS="-DSSL_EXPERIMENTAL_ENGINE"
export CFLAGS CPPFLAGS

function mpmbuild()
{
mpm=$1; shift
mkdir $mpm; pushd $mpm
../configure \
 	--prefix=%{_sysconfdir}/httpd \
 	--exec-prefix=%{_prefix} \
 	--bindir=%{_bindir} \
 	--sbindir=%{_sbindir} \
 	--mandir=%{_mandir} \
	--libdir=%{_libdir} \
	--sysconfdir=%{_sysconfdir}/httpd/conf \
	--includedir=%{_includedir}/httpd \
	--libexecdir=%{_libdir}/httpd/modules \
	--datadir=%{contentdir} \
        --with-installbuilddir=%{_libdir}/httpd/build \
	--with-mpm=$mpm \
        --with-apr=%{_prefix} --with-apr-util=%{_prefix} \
	--enable-suexec --with-suexec \
	--with-suexec-caller=%{suexec_caller} \
	--with-suexec-docroot=%{contentdir} \
	--with-suexec-logfile=%{_localstatedir}/log/httpd/suexec.log \
	--with-suexec-bin=%{_sbindir}/suexec \
	--with-suexec-uidmin=500 --with-suexec-gidmin=100 \
	$*

make %{?_smp_mflags}
popd
}

# Only bother enabling optional modules for main build.
mpmbuild prefork --enable-mods-shared=all \
	--enable-ssl --with-ssl --enable-distcache \
	--enable-deflate \
	--enable-proxy --enable-proxy-connect \
	--enable-proxy-http --enable-proxy-ftp \
        --enable-cache --enable-mem-cache \
        --enable-file-cache --enable-disk-cache \
        --enable-ldap --enable-auth-ldap \
        --enable-logio --enable-cgid

# To prevent most modules being built statically into httpd.worker, 
# easiest way seems to be enable them shared.
mpmbuild worker --enable-mods-shared=all

%install
rm -rf $RPM_BUILD_ROOT

# Classify ab and logresolve as section 1 commands, as they are in /usr/bin
mv docs/man/ab.8 docs/man/ab.1
mv docs/man/logresolve.8 docs/man/logresolve.1

pushd prefork
make DESTDIR=$RPM_BUILD_ROOT install
popd
# install worker binary
install -m 755 worker/httpd $RPM_BUILD_ROOT%{_sbindir}/httpd.worker

# link to system pcreposix.h
ln -s ../pcreposix.h $RPM_BUILD_ROOT%{_includedir}/httpd/pcreposix.h

# install conf file/directory
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/README.confd \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/README
for f in ssl.conf welcome.conf manual.conf; do
  install -m 644 $RPM_SOURCE_DIR/$f $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/$f
done

rm $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/*.conf
install -m 644 $RPM_SOURCE_DIR/httpd.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/httpd.conf

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 $RPM_SOURCE_DIR/httpd.sysconf \
   $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/httpd

# for holding mod_dav lock database
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/dav

# create a prototype session cache
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/mod_ssl
touch $RPM_BUILD_ROOT%{_localstatedir}/cache/mod_ssl/scache.{dir,pag,sem}

# create cache root
mkdir $RPM_BUILD_ROOT%{_localstatedir}/cache/mod_proxy

# move utilities to /usr/bin
mv $RPM_BUILD_ROOT%{_sbindir}/{ab,htdbm,logresolve,htpasswd,htdigest} \
   $RPM_BUILD_ROOT%{_bindir}

# move builddir to the right place
mv $RPM_BUILD_ROOT%{contentdir}/build $RPM_BUILD_ROOT%{_libdir}/httpd/build

# point to the correct libtool
apr_libtool=`apr-config --apr-libtool | sed -e 's|/bin/sh ||'`
ln -s ../../../..${apr_libtool} $RPM_BUILD_ROOT%{_libdir}/httpd/build/libtool

# Install and sanitize config_vars file: relocate the build directory into 
# libdir; reference correct libtool; fix EXTRA_INCLUDES
sed -e "s|%{contentdir}/build|%{_libdir}/httpd/build|g" \
    -e "/AP_LIBS/d" -e "/abs_srcdir/d" \
    -e "/^LIBTOOL/s|/bin/sh /[^ ]*/libtool|/bin/sh ${apr_libtool}|" \
    -e "/^installbuilddir/s| = .*$| = /etc/httpd/build|" \
    -e "s|^EXTRA_INCLUDES.*$|EXTRA_INCLUDES = -I\$(includedir) -I\$(APR_INCLUDEDIR) -I%{_includedir}/openssl|g" \
  < prefork/build/config_vars.mk \
  > $RPM_BUILD_ROOT%{_libdir}/httpd/build/config_vars.mk
install -m 644 build/special.mk \
    $RPM_BUILD_ROOT%{_libdir}/httpd/build/special.mk

# Make the MMN accessible to module packages
echo %{mmn} > $RPM_BUILD_ROOT%{_includedir}/httpd/.mmn

# docroot
mkdir $RPM_BUILD_ROOT%{contentdir}/html
install -m 644 $RPM_SOURCE_DIR/index.html \
	$RPM_BUILD_ROOT%{contentdir}/error/noindex.html

# remove manual sources
find $RPM_BUILD_ROOT%{contentdir}/manual \( \
    -name \*.xml -o -name \*.xml.* -o -name \*.ent -o -name \*.xsl -o -name \*.dtd \
    \) -print0 | xargs -0 rm -f

install -m 644 $RPM_SOURCE_DIR/powered_by_fedora.png \
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

# Remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.exp \
      $RPM_BUILD_ROOT/etc/httpd/conf/mime.types \
      $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.exp \
      $RPM_BUILD_ROOT%{_libdir}/httpd/build/config.nice \
      $RPM_BUILD_ROOT%{_bindir}/ap?-config \
      $RPM_BUILD_ROOT%{_sbindir}/{checkgid,dbmmanage,envvars*} \
      $RPM_BUILD_ROOT%{contentdir}/htdocs/* \
      $RPM_BUILD_ROOT%{_mandir}/man1/dbmmanage.* \
      $RPM_BUILD_ROOT%{contentdir}/cgi-bin/*

# Make suexec a+rw so it can be stripped.  %%files lists real permissions
chmod 755 $RPM_BUILD_ROOT%{_sbindir}/suexec

%pre
# Add the "apache" user
/usr/sbin/useradd -c "Apache" -u 48 \
	-s /sbin/nologin -r -d %{contentdir} apache 2> /dev/null || :

%triggerpostun -- apache < 2.0, stronghold-apache < 2.0
/sbin/chkconfig --add httpd

# Prevent removal of index.html on upgrades from 1.3
%triggerun -- apache < 2.0, stronghold-apache < 2.0
if [ -r %{contentdir}/index.html -a ! -r %{contentdir}/index.html.rpmold ]; then
  mv %{contentdir}/index.html %{contentdir}/index.html.rpmold
fi

%post
# Register the httpd service
/sbin/chkconfig --add httpd

%preun
if [ $1 = 0 ]; then
	/sbin/service httpd stop > /dev/null 2>&1
	/sbin/chkconfig --del httpd
fi

%define sslcert %{_sysconfdir}/pki/tls/certs/localhost.crt
%define sslkey %{_sysconfdir}/pki/tls/private/localhost.key

%post -n mod_ssl
umask 077

if [ ! -f %{sslkey} ] ; then
%{_bindir}/openssl genrsa -rand /proc/apm:/proc/cpuinfo:/proc/dma:/proc/filesystems:/proc/interrupts:/proc/ioports:/proc/pci:/proc/rtc:/proc/uptime 1024 > %{sslkey} 2> /dev/null
fi

FQDN=`hostname`
if [ "x${FQDN}" = "x" ]; then
   FQDN=localhost.localdomain
fi

if [ ! -f %{sslcert} ] ; then
cat << EOF | %{_bindir}/openssl req -new -key %{sslkey} \
         -x509 -days 365 -set_serial $RANDOM \
         -out %{sslcert} 2>/dev/null
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
${FQDN}
root@${FQDN}
EOF
fi

%check
# Check the built modules are all PIC
if readelf -d $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.so | grep TEXTREL; then
   : modules contain non-relocatable code
   exit 1
fi

# Verify that the same modules were built into the two httpd binaries
./prefork/httpd -l | grep -v prefork > prefork.mods
./worker/httpd -l | grep -v worker > worker.mods
if ! diff -u prefork.mods worker.mods; then
  : Different modules built into httpd binaries, will not proceed
  exit 1
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%doc ABOUT_APACHE README CHANGES LICENSE VERSIONING NOTICE
%doc migration.html migration.css

%dir %{_sysconfdir}/httpd
%{_sysconfdir}/httpd/modules
%{_sysconfdir}/httpd/logs
%{_sysconfdir}/httpd/run
%dir %{_sysconfdir}/httpd/conf
%config(noreplace) %{_sysconfdir}/httpd/conf/*.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/welcome.conf
%config(noreplace) %{_sysconfdir}/httpd/conf/magic

%config(noreplace) %{_sysconfdir}/logrotate.d/httpd
%config %{_sysconfdir}/rc.d/init.d/httpd

%dir %{_sysconfdir}/httpd/conf.d
%{_sysconfdir}/httpd/conf.d/README

%config(noreplace) %{_sysconfdir}/sysconfig/httpd

%{_bindir}/ab
%{_bindir}/ht*
%{_bindir}/logresolve
%{_sbindir}/httpd
%{_sbindir}/httpd.worker
%{_sbindir}/apachectl
%{_sbindir}/rotatelogs
%attr(4510,root,%{suexec_caller}) %{_sbindir}/suexec

%dir %{_libdir}/httpd
%dir %{_libdir}/httpd/modules
%{_libdir}/httpd/modules/mod*.so
%exclude %{_libdir}/httpd/modules/mod_ssl.so

%dir %{contentdir}
%dir %{contentdir}/cgi-bin
%dir %{contentdir}/html
%dir %{contentdir}/icons
%dir %{contentdir}/error
%dir %{contentdir}/error/include
%{contentdir}/icons/*
%{contentdir}/error/README
%{contentdir}/error/noindex.html
%config %{contentdir}/error/*.var
%config %{contentdir}/error/include/*.html

%attr(0700,root,root) %dir %{_localstatedir}/log/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/lib/dav
%attr(0700,apache,apache) %dir %{_localstatedir}/cache/mod_proxy

%{_mandir}/man?/*
%exclude %{_mandir}/man8/apxs.8*

%files manual
%defattr(-,root,root)
%{contentdir}/manual
%config(noreplace) %{_sysconfdir}/httpd/conf.d/manual.conf

%files -n mod_ssl
%defattr(-,root,root)
%{_libdir}/httpd/modules/mod_ssl.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/ssl.conf
%attr(0700,apache,root) %dir %{_localstatedir}/cache/mod_ssl
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.dir
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.pag
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.sem

%files devel
%defattr(-,root,root)
%{_includedir}/httpd
%{_sysconfdir}/httpd/build
%{_sbindir}/apxs
%{_mandir}/man8/apxs.8*
%dir %{_libdir}/httpd/build
%{_libdir}/httpd/build/*.mk
%{_libdir}/httpd/build/instdso.sh
%{_libdir}/httpd/build/libtool

%changelog
* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> 2.0.54-16
- rebuilt against new openssl

* Thu Nov  3 2005 Joe Orton <jorton@redhat.com> 2.0.54-15
- log notice giving SELinux context at startup if enabled
- drop SSLv2 and restrict default cipher suite in default
 SSL configuration

* Thu Oct 20 2005 Joe Orton <jorton@redhat.com> 2.0.54-14
- mod_ssl: add security fix for SSLVerifyClient (CVE-2005-2700)
- add security fix for byterange filter DoS (CVE-2005-2728)
- add security fix for C-L vs T-E handling (CVE-2005-2088)
- mod_ssl: add security fix for CRL overflow (CVE-2005-1268)
- mod_ldap/mod_auth_ldap: add fixes from 2.0.x branch (upstream #34209 etc)
- add fix for dummy connection handling (#167425)
- mod_auth_digest: fix hostinfo comparison in CONNECT requests
- mod_include: fix variable corruption in nested includes (upstream #12655)
- mod_ssl: add fix for handling non-blocking reads
- mod_ssl: fix to enable output buffering (upstream #35279)
- mod_ssl: buffer request bodies for per-location renegotiation (upstream #12355)

* Sat Aug 13 2005 Joe Orton <jorton@redhat.com> 2.0.54-13
- don't load by default: mod_cern_meta, mod_asis
- do load by default: mod_ext_filter (#165893)

* Thu Jul 28 2005 Joe Orton <jorton@redhat.com> 2.0.54-12
- drop broken epoch deps

* Thu Jun 30 2005 Joe Orton <jorton@redhat.com> 2.0.54-11
- mod_dav_fs: fix uninitialized variable (#162144)
- add epoch to dependencies as appropriate
- mod_ssl: drop dependencies on dev, make
- mod_ssl: mark post script dependencies as such

* Mon May 23 2005 Joe Orton <jorton@redhat.com> 2.0.54-10
- remove broken symlink (Robert Scheck, #158404)

* Wed May 18 2005 Joe Orton <jorton@redhat.com> 2.0.54-9
- add piped logger fixes (w/Jeff Trawick)

* Mon May  9 2005 Joe Orton <jorton@redhat.com> 2.0.54-8
- drop old "powered by Red Hat" logos

* Wed May  4 2005 Joe Orton <jorton@redhat.com> 2.0.54-7
- mod_userdir: fix memory allocation issue (upstream #34588)
- mod_ldap: fix memory corruption issue (Brad Nicholes, upstream #34618)

* Tue Apr 26 2005 Joe Orton <jorton@redhat.com> 2.0.54-6
- fix key/cert locations in post script

* Mon Apr 25 2005 Joe Orton <jorton@redhat.com> 2.0.54-5
- create default dummy cert in /etc/pki/tls
- use a pseudo-random serial number on the dummy cert
- change default ssl.conf to point at /etc/pki/tls
- merge back -suexec subpackage; SELinux policy can now be
  used to persistently disable suexec (#155716)
- drop /etc/httpd/conf/ssl.* directories and Makefiles
- unconditionally enable PIE support
- mod_ssl: fix for picking up -shutdown options (upstream #34452)

* Mon Apr 18 2005 Joe Orton <jorton@redhat.com> 2.0.54-4
- replace PreReq with Requires(pre) 

* Mon Apr 18 2005 Joe Orton <jorton@redhat.com> 2.0.54-3
- update to 2.0.54

* Tue Mar 29 2005 Joe Orton <jorton@redhat.com> 2.0.53-6
- update default httpd.conf:
 * clarify the comments on AddDefaultCharset usage (#135821)
 * remove all the AddCharset default extensions
 * don't load mod_imap by default
 * synch with upstream 2.0.53 httpd-std.conf
- mod_ssl: set user from SSLUserName in access hook (upstream #31418)
- htdigest: fix permissions of created files (upstream #33765)
- remove htsslpass

* Wed Mar  2 2005 Joe Orton <jorton@redhat.com> 2.0.53-5
- apachectl: restore use of $OPTIONS again

* Wed Feb  9 2005 Joe Orton <jorton@redhat.com> 2.0.53-4
- update to 2.0.53
- move prefork/worker modules comparison to %%check

* Mon Feb  7 2005 Joe Orton <jorton@redhat.com> 2.0.52-7
- fix cosmetic issues in "service httpd reload"
- move User/Group higher in httpd.conf (#146793)
- load mod_logio by default in httpd.conf
- apachectl: update for correct libselinux tools locations

* Tue Nov 16 2004 Joe Orton <jorton@redhat.com> 2.0.52-6
- add security fix for CVE CAN-2004-0942 (memory consumption DoS)
- SELinux: run httpd -t under runcon in configtest (Steven Smalley)
- fix SSLSessionCache comment for distcache in ssl.conf
- restart using SIGHUP not SIGUSR1 after logrotate
- add ap_save_brigade fix (upstream #31247)
- mod_ssl: fix possible segfault in auth hook (upstream #31848)
- add htsslpass(1) and configure as default SSLPassPhraseDialog (#128677)
- apachectl: restore use of $OPTIONS
- apachectl, httpd.init: refuse to restart if $HTTPD -t fails
- apachectl: run $HTTPD -t in user SELinux context for configtest
- update for pcre-5.0 header locations

* Sat Nov 13 2004 Jeff Johnson <jbj@redhat.com> 2.0.52-5
- rebuild against db-4.3.21 aware apr-util.

* Thu Nov 11 2004 Jeff Johnson <jbj@jbj.org> 2.0.52-4
- rebuild against db-4.3-21.

* Thu Sep 28 2004 Joe Orton <jorton@redhat.com> 2.0.52-3
- add dummy connection address fixes from HEAD
- mod_ssl: add security fix for CAN-2004-0885

* Tue Sep 28 2004 Joe Orton <jorton@redhat.com> 2.0.52-2
- update to 2.0.52

* Tue Sep 21 2004 Joe Orton <jorton@redhat.com> 2.0.51-6
- fix 2.0.51 regression in Satisfy merging (CAN-2004-0811)

* Sat Sep 18 2004 Joe Orton <jorton@redhat.com> 2.0.51-5
- switch to Jeff Trawick's child reclaim timing logic patch
- migration guide updates

* Thu Sep 16 2004 Joe Orton <jorton@redhat.com> 2.0.51-4
- fix pcre includes

* Thu Sep 16 2004 Joe Orton <jorton@redhat.com> 2.0.51-3
- update to 2.0.51

* Tue Sep 14 2004 Joe Orton <jorton@redhat.com> 2.0.50-8
- add improved child reclaim timing logic (#119128/#132360)
- add BuildRequire zlib-devel for mod_deflate

* Wed Sep  8 2004 Joe Orton <jorton@redhat.com> 2.0.50-7
- prereq rather than just require httpd from -suexec (#132045)

* Sun Sep  5 2004 Joe Orton <jorton@redhat.com> 2.0.50-6
- include /etc/sysconfig/httpd template (#112085)
- pass $OPTIONS in httpd invocations in apachectl (#115910)
- do not pass $OPTIONS to apachectl from init script
- start httpd in C locale by default from apachectl

* Wed Sep  1 2004 Joe Orton <jorton@redhat.com> 2.0.50-5
- move manual configuration into conf.d/manual.conf (#131208)
- add test_hook from HEAD, -t -DDUMP_CERTS for mod_ssl
- document AddDefaultCharset change since 1.3 in migration.html

* Tue Aug 17 2004 Joe Orton <jorton@redhat.com> 2.0.50-4
- start httpd in the C locale by default (#128002)
- fix CustomLog comments in default httpd.conf (#43223)
- ensure correct mod_suexec vs mod_userdir hook ordering 
  (Joshua Slive, upstream #18156)

* Tue Jun 29 2004 Joe Orton <jorton@redhat.com> 2.0.50-3
- update -proxy11 patch
- explain where suexec went if SuexecUserGroup is used but
  /usr/sbin/suexec is not found

* Tue Jun 29 2004 Joe Orton <jorton@redhat.com> 2.0.50-1
- update to 2.0.50

* Mon Jun 21 2004 Joe Orton <jorton@redhat.com> 2.0.49-8
- split out suexec into httpd-suexec package (#77972)
- link to system pcreposix.h to fix including httpd.h

* Wed Jun 16 2004 Joe Orton <jorton@redhat.com> 2.0.49-7
- don't install or use bundled pcreposix.h
- bump default MaxClients to 256
- drop default Timeout to 2 minutes
- merge from upstream:
 * add fix for VirtualHost multiple address handling (Jeff Trawick)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> 2.0.49-6
- rebuilt

* Thu Jun 10 2004 Joe Orton <jorton@redhat.com> 2.0.49-5
- remove comments about ScoreBoardFile in httpd.conf
- avoid redundant name lookup in pod code
- mod_headers: add %{...}s feature for using SSL variables
- mod_autoindex: don't truncate output on stat() failure (#117959)
- mod_ssl: fix shmcb corruption with small caches (Geoff Thorpe)
- mod_ssl: security fix for overflow in FakeBasicAuth (CVE CAN-2004-0488)
- mod_deflate: fix memory consumption for large responses
- check that suexec is setuid root (André Malo)
- worker: add ThreadStackSize (Jeff Trawick) and ThreadGuardSize directives

* Thu May  6 2004 Joe Orton <jorton@redhat.com> 2.0.49-4
- make "noindex" page valid XHTML 1.1 (Pascal Volk, #122020)
- fix SEGV with no Listen directives (Michael Corcoran)
- mod_cgi: synch with 2.0 backport proposed upstream

* Thu Apr 22 2004 Joe Orton <jorton@redhat.com> 2.0.49-3
- conflict with older pcre (#121531)
- include mod_ext_filter
- mod_cgi: handle concurrent stderr/stdout from script

* Fri Mar 26 2004 Joe Orton <jorton@redhat.com> 2.0.49-2
- mod_ssl: fix session cache memory leak (Madhu Mathihalli)
- mod_ssl: fix SEGV when trying to shutdown during pool cleanup
- merge the mod_proxy HTTP/1.1-compliance fixes
- apply fix for #118020

* Thu Mar 18 2004 Joe Orton <jorton@redhat.com> 2.0.49-1
- update to 2.0.49 (#118798, thanks to Robert Scheck)
- only link ab and mod_ssl against SSL_LIBS
- open log files using APR_LARGEFILE where available

* Wed Mar 17 2004 Joe Orton <jorton@redhat.com> 2.0.48-18
- add fix for #118020
- ssl.conf tweaks: seed SSL PRNG with 256 bytes from /dev/urandom

* Mon Mar 15 2004 Joe Orton <jorton@redhat.com> 2.0.48-17
- use "SSLMutex default" in default ssl.conf
- limit to 128K XML request bodies in default httpd.conf; fix to 
  give a 413 error not a 400 if the limit is exceeded
- mod_rewrite: add %%{SSL:...} and %%{HTTPS} variable lookups
- mod_dav: propagate executable property across COPY/MOVE
- mod_dav: give 507 on out-of-space errors in more places
- mod_ssl: add ssl_is_https optional function
- mod_ssl: support indexed lookup of DN components
- mod_ssl: optimised variable lookup
- mod_ssl: install only minimal mod_ssl.h
- worker: fix potential hang at restart

* Tue Mar  2 2004 Elliot Lee <sopwith@redhat.com> 2.0.48-16.1
- Rebuilt.

* Mon Feb 23 2004 Joe Orton <jorton@redhat.com> 2.0.48-16
- fix apxs -q installbuilddir
- really update to ab from HEAD
- remove check that accept() returns an fd < FD_SETSIZE 

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 2.0.48-15
- Rebuilt.

* Tue Feb  3 2004 Joe Orton <jorton@redhat.com> 2.0.48-14
- mod_dav: fix 401 on destination and reject unescaped fragment in URI
- remove redundant ldconfig invocation from mod_ssl %%post
- remove unnecessary -headusage patch

* Fri Jan 30 2004 Joe Orton <jorton@redhat.com> 2.0.48-13
- allow further customisation of init script (Peter Bieringer, #114619)
- worker fixes from upstream
- use basename(filename) in APLOG_MARK to reduce noise levels at 
  "LogLevel debug"

* Wed Jan 28 2004 Joe Orton <jorton@redhat.com> 2.0.48-12
- mod_ssl: cosmetic tweaks for pass phrase prompting
- simplify rebranding a little

* Tue Jan 27 2004 Joe Orton <jorton@redhat.com> 2.0.48-11
- trim pre-2.0 history from CHANGES to limit size

* Tue Jan 27 2004 Joe Orton <jorton@redhat.com> 2.0.48-10
- update to ab from HEAD
- remove dbmmanage man page (part of #114080)
- mod_ssl: fix streaming nph- CGI scripts over SSL
- mod_autoindex: fixes from 2.0 branch (André Malo)
- add NameVirtualHost vs mod_ssl warning to httpd.conf (#114315)
- mod_proxy: HTTP/1.1-compliance fixes from HEAD

* Tue Jan 20 2004 Joe Orton <jorton@redhat.com> 2.0.48-9
- use a large BSS in the test PIE executable to trigger bugs early
- tighten check on CPP output in MMN check (#113934)

* Mon Jan 19 2004 Joe Orton <jorton@redhat.com> 2.0.48-8
- add man page fixes
- mod_include: use parser rewrite+fixes from 2.0 branch (André Malo et al)
- mod_ssl: add distcache support (Geoff Thorpe)
- mod_ssl: SSL variable handling fixes for non-SSL connections (various)
- allow linking modules against specific libraries found during configure

* Mon Jan 19 2004 Joe Orton <jorton@redhat.com> 2.0.48-7
- hack to ensure that /usr/sbin/suexec gets stripped
- merges from upstream:
 * fix for CVE CAN-2003-0020 (André Malo)
 * open log files read-only (Jeff Trawick)
 * mod_cgi: fix logging of script exec failure messages (Jeff Trawick)
 * mod_proxy: fix leak in request body handling (Larry Toppi)
- merges from Taroon:
 * move away /var/www/html/index.html before upgrade from 1.3 (#70705)
 * allow upgrade from Stronghold 4.0
 * migration guide updates 
 * mod_log_config: fix logging of timezone (upstream #23642)
 * mod_ssl: restore readable error descriptions in error log

* Mon Jan 19 2004 Joe Orton <jorton@redhat.com> 2.0.48-6
- fix httpd.init issues reported by Behdad Esfahbod
- add fix for mod_usertrack (#113269)
- automatically raise RLIMIT_CORE if CoreDumpDirectory is used
- emit warning at end of %%prep if PIE support is not enabled
- add symlink to libtool script from build directory (#113720)
- don't link suexec against the world

* Sun Jan 04 2004 Joe Orton <jorton@redhat.com> 2.0.48-5
- use graceful restart in logrotate
- bump default MaxRequestsPerChild for prefork to 4000
- move vendor string for Server header into spec file
- include mod_status extension hook and use it in mod_ssl to include
  SSL session cache statistics in server-status output

* Thu Dec 18 2003 Joe Orton <jorton@redhat.com> 2.0.48-4
- rebuild

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 2.0.48-3
- rebuild against db-4.2.52.

* Tue Oct 28 2003 Joe Orton <jorton@redhat.com> 2.0.48-2
- update to 2.0.48
- includes security fix for CVE CAN-2003-0542
- include mpm*.h to fix mod_fastcgi build (#108080)
- increase DYNAMIC_MODULE_LIMIT to 128
- re-enable ap_hack_* export trimming patch
- only use -export-dynamic when linking httpd, not suexec etc
- don't load mod_unique_id by default

* Thu Oct 23 2003 Joe Orton <jorton@redhat.com> 2.0.47-10
- httpd.conf: configure test page in welcome.conf, load suexec, 
 don't use custom error docs by default, sync with upstream.
- add "Powered by Fedora" icon (Garrett LeSage)
- migration guide updates
- drop mod_cgid
- enable SSL_EXPERIMENTAL_ENGINE (#106858)
- drop minimum suexec gid to 100 (#74753, #107083)
- speed up graceful restarts in prefork (#105725)
- mod_ssl fixes

* Wed Oct 22 2003 Joe Orton <jorton@redhat.com> 2.0.47-9
- updated index.html (Matt Wilson, #107378)
- change server version string comment to "(Fedora)"

* Mon Oct 13 2003 Jeff Johnson <jbj@jbj.org> 2.0.47-8.1
- rebuild against db-4.2.42.

* Wed Oct  8 2003 Joe Orton <jorton@redhat.com> 2.0.47-8
- use -fPIE not -fpie to fix s390x (Florian La Roche)
- include VERSIONING in docdir

* Mon Oct  6 2003 Joe Orton <jorton@redhat.com> 2.0.47-7
- enable PIE support
- include bug fix for #78019

* Mon Sep  8 2003 Joe Orton <jorton@redhat.com> 2.0.47-6
- update httpd.conf for manual changes (alietss@yahoo.com, #101015)
- use anonymous shm for LDAP auth cache (#103566)

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 2.0.47-5
- include unixd.h again
- fix EXTRA_INCLUDES

* Mon Jul 28 2003 Joe Orton <jorton@redhat.com> 2.0.47-4
- add mod_include fixes from upstream
- httpd.conf updates: wording fixes from upstream; load
  mod_deflate by default, update AddLanguage section (#98455)
- don't add eNULL cipher in default ssl.conf (#98401)
- only bind to IPv4 addresses in default config (#98916)

* Thu Jul 24 2003 Joe Orton <jorton@redhat.com> 2.0.47-3
- fix for segfaults in php-snmp init (#97207)

* Wed Jul 23 2003 Joe Orton <jorton@redhat.com> 2.0.47-2
- fix apxs -c again

* Mon Jul 14 2003 Joe Orton <jorton@redhat.com> 2.0.47-1
- update to 2.0.47
- add mod_logio (#100436)
- remove Vendor tag

* Thu Jul 10 2003 Joe Orton <jorton@redhat.com> 2.0.45-14
- use libtool script included in apr
- fix apxs -q LIBTOOL (more #92313)

* Tue Jul  8 2003 Joe Orton <jorton@redhat.com> 2.0.45-13
- use system pcre library

* Thu Jul  3 2003 Joe Orton <jorton@redhat.com> 2.0.45-12
- remove some installed headers
- fix for use of libtool 1.5

* Wed Jun 5 2003 Elliot Lee <sopwith@redhat.com>
- Rebuilt.

* Thu Jun  5 2003 Joe Orton <jorton@redhat.com> 2.0.45-10
- fix apxs -g (#92313)

* Sat May 31 2003 Joe Orton <jorton@redhat.com> 2.0.45-9
- trim manual sources properly
- remove ExcludeArch

* Thu May 29 2003 Joe Orton <jorton@redhat.com> 2.0.45-8
- rebuild

* Mon May 19 2003 Joe Orton <jorton@redhat.com> 2.0.45-6
- don't load /usr/sbin/envvars from apxs
- add fix for mod_dav_fs namespace handling
- add fix for mod_dav If header etag comparison
- remove irrelevant warning from mod_proxy
- don't conflict with thttpd (#91422)

* Sun May 18 2003 Joe Orton <jorton@redhat.com> 2.0.45-5
- don't package any XML sources in httpd-manual
- fix examples in default httpd.conf for enabling caching

* Sun May 18 2003 Joe Orton <jorton@redhat.com> 2.0.45-4
- change default charset to UTF-8 (#88964)

* Thu May 15 2003 Joe Orton <jorton@redhat.com> 2.0.45-3
- update httpd.conf for changes from default in 2.0.45
- include conf.d/*.conf after loading standard modules
- include LDAP and cache modules (#75370, #88277)
- run buildconf in %%build not %%prep

* Tue May 13 2003 Joe Orton <jorton@redhat.com> 2.0.45-2
- have apxs always use /usr/bin/libtool

* Mon May 5 2003 Joe Orton <jorton@redhat.com> 2.0.45-1
- update to 2.0.45 (#82227)
- use separate apr, apr-util packages (#74951)
- mark logrotate file as noreplace (#85654)
- mark all of /var/www/error as %%config-not-noreplace
- remove dates from error pages (#86474)
- don't enable mod_cgid for worker MPM (#88819)

* Wed Apr 30 2003 Elliot Lee <sopwith@redhat.com> 2.0.40-22
- headusage patch to fix build on ppc64 etc.

* Tue Apr  1 2003 Joe Orton <jorton@redhat.com> 2.0.40-21.1
- add security fixes for CAN-2003-0020, CAN-2003-0132, CAN-2003-0083
- add security fix for file descriptor leaks, #82142
- add bug fix for #82587

* Mon Feb 24 2003 Joe Orton <jorton@redhat.com> 2.0.40-21
- add security fix for CAN-2003-0020; replace non-printable characters
  with '!' when printing to error log.
- disable debuginfo on IA64.

* Tue Feb 11 2003 Joe Orton <jorton@redhat.com> 2.0.40-20
- disable POSIX semaphores to support 2.4.18 kernel (#83324)

* Wed Jan 29 2003 Joe Orton <jorton@redhat.com> 2.0.40-19
- require xmlto 0.0.11 or later
- fix apr_strerror on glibc2.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 2.0.40-18
- Rebuilt.

* Thu Jan 16 2003 Joe Orton <jorton@redhat.com> 2.0.40-17
- add mod_cgid and httpd binary built with worker MPM (#75496)
- allow choice of httpd binary in init script
- pick appropriate CGI module based on loaded MPM in httpd.conf
- source /etc/sysconfig/httpd in apachectl to get httpd choice
- make "apachectl status" fail gracefully when links isn't found (#78159)

* Mon Jan 13 2003 Joe Orton <jorton@redhat.com> 2.0.40-16
- rebuild for OpenSSL 0.9.7

* Fri Jan  3 2003 Joe Orton <jorton@redhat.com> 2.0.40-15
- fix possible infinite recursion in config dir processing (#77206)
- fix memory leaks in request body processing (#79282)

* Thu Dec 12 2002 Joe Orton <jorton@redhat.com> 2.0.40-14
- remove unstable shmht session cache from mod_ssl
- get SSL libs from pkg-config if available (Nalin Dahyabhai)
- stop "apxs -a -i" from inserting AddModule into httpd.conf (#78676)

* Wed Nov  6 2002 Joe Orton <jorton@redhat.com> 2.0.40-13
- fix location of installbuilddir in apxs when libdir!=/usr/lib

* Wed Nov  6 2002 Joe Orton <jorton@redhat.com> 2.0.40-12
- pass libdir to configure; clean up config_vars.mk
- package instdso.sh, fixing apxs -i (#73428)
- prevent build if upstream MMN differs from mmn macro
- remove installed but unpackaged files

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
