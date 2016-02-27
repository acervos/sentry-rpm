Name: sentry
Version: 1
Release: 1%{?dist}
Group: Application/Web
License: MIT
Summary: sentry
Source0: sentry.tar.gz
Source1: sentry.service
Source2: supervisord.conf

Requires: cloud-httpd24-ssl-services-devs-staff libxslt-devel libxml2-devel zlib-devel libffi-devel openssl-devel libpqxx-devel libyaml-devel gcc postgresql-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: x86_64

%description
Sentry exception service

%prep
%setup -T -c mbt

%install
mkdir -p %{buildroot}/etc/sentry/ %{buildroot}/usr/lib/systemd/system/ %{buildroot}/www/sentry %{buildroot}/etc/sysconfig/httpd.d %{buildroot}/etc/bake-scripts/sentry
cp %{Source1} %{buildroot}/usr/lib/systemd/system/
cp %{Source2} %{buildroot}/etc/
tar -C %{buildroot}/www/sentry -xzf %{SOURCE0} --strip 1

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -d / -s /sbin/nologin %{name}

%post
/bin/chmod a+x /www/sentry/bin/*
/bin/chown -R %{name}:%{name} /www/sentry/
/bin/systemctl enable sentry

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun

%clean
rm -rf %{buildroot}

%files
%defattr(644, root, root, 755)
/www/sentry
/usr/lib/systemd/system/sentry.service
/etc/sentry/*
/etc/supervisord.conf
/etc/sysconfig/httpd.d/ports.conf
%defattr(0755, root, root, 0755)
/etc/bake-scripts/sentry/
