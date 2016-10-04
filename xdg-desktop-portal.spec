Summary:	Portal frontend service to Flatpak
Name:		xdg-desktop-portal
Version:	0.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://github.com/flatpak/xdg-desktop-portal/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3c4393f513b833c9e464820479c7db19
URL:		https://github.com/flatpak/xdg-desktop-portal/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	flatpak-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig >= 1:0.24
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-desktop-portal works by exposing a series of D-Bus interfaces
known as portals under a well-known name
(org.freedesktop.portal.Desktop) and object path
(/org/freedesktop/portal/desktop). The portal interfaces include APIs
for file access, opening URIs, printing and others.

%package devel
Summary:	Development files for xdg-desktop-portal
Group:		Development/Libraries
Requires:	flatpak-devel
Requires:	glib2-devel

%description devel
Development files for xdg-desktop-portal.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/xdg-desktop-portal

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md doc/*.html doc/*.css
%attr(755,root,root) %{_libexecdir}/xdg-desktop-portal
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Access.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.AppChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.FileChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Inhibit.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Notification.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Print.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Request.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Device.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.FileChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Inhibit.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.NetworkMonitor.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Notification.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.OpenURI.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Print.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.ProxyResolver.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Request.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Screenshot.xml
%{_datadir}/dbus-1/services/org.freedesktop.portal.Desktop.service

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/xdg-desktop-portal.pc
