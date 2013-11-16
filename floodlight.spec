Summary: Floodlight Open SDN Controller
Name: floodlight
Version: 0.91
Release: 1%{?dist}
License: Apache 2.0
Vendor: Bigswitch Networks
Group: System Environment/Daemons
URL: http://www.projectfloodlight.org/floodlight/
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch:  noarch
Source: floodlight-source-%{version}.zip
Requires: ant


%description
Floodlight is a high performance Java based OpenFlow controller originally
written by David Erickson at Stanford University.
 
Floodlight supports a broad range of virtual and physical OpenFlow switches
and has rich support for mixed OpenFlow and non-OpenFlow networks supporting
management of multiple islands of OpenFlow switches.


%prep
%setup -n %{name}-%{version} 


%build
ant


%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 debian/misc/bin/authtool %{buildroot}%{_bindir}/authtool
install -m 0755 debian/misc/bin/bootstraptool %{buildroot}%{_bindir}/bootstraptool
install -m 0755 debian/misc/bin/floodlight %{buildroot}%{_bindir}/floodlight
install -m 0755 debian/misc/bin/syncclient %{buildroot}%{_bindir}/syncclient

mkdir -p %{buildroot}/var/log/floodlight
mkdir -p %{buildroot}/usr/share/floodlight/java
install -m 0644 target/floodlight.jar %{buildroot}/usr/share/floodlight/java/floodlight.jar

mkdir -p %{buildroot}/usr/share/doc/floodlight
cat README.md | gzip -c > %{buildroot}/usr/share/doc/floodlight/README.md.gz
cat LICENSE.txt | gzip -c > %{buildroot}/usr/share/doc/floodlight/LICENSE.txt.gz
cat NOTICE.txt | gzip -c > %{buildroot}/usr/share/doc/floodlight/NOTICE.txt.gz

mkdir -p %{buildroot}/etc/floodlight
cp debian/misc/logback.xml %{buildroot}/etc/floodlight/logback.xml
cp target/bin/floodlightdefault.properties %{buildroot}/etc/floodlight/floodlightdefault.properties

mkdir -p %{buildroot}/etc/logrotate.d
cp debian/misc/logrotate/floodlight %{buildroot}/etc/logrotate.d/floodlight

mkdir -p %{buildroot}/%{_mandir}/man1
cat debian/control/floodlight.1 | gzip -c > %{buildroot}%{_mandir}/man1/floodlight.1.gz

mkdir -p %{buildroot}/etc/rsyslog.d
cp debian/misc/rsyslog/10-floodlight.conf %{buildroot}/etc/rsyslog.d/10-floodlight.conf

mkdir -p %{buildroot}/etc/sysconfig/floodlight
cp debian/misc/default/floodlight %{buildroot}/etc/sysconfig/floodlight

%clean
rm -rf %{buildroot}

%files
%{_bindir}/authtool
%{_bindir}/bootstraptool
%{_bindir}/floodlight
%{_bindir}/syncclient
/usr/share/floodlight/java/floodlight.jar
%config /etc/floodlight/floodlightdefault.properties
%config /etc/floodlight/logback.xml
%config /etc/logrotate.d/floodlight
%config /etc/rsyslog.d/10-floodlight.conf
%config /etc/sysconfig/floodlight
%docdir %{_docdir}
%doc %{_docdir}/floodlight/README.md.gz
%doc %{_docdir}/floodlight/LICENSE.txt.gz
%doc %{_docdir}/floodlight/NOTICE.txt.gz
%doc %{_mandir}/man1/floodlight.1.gz

%changelog

