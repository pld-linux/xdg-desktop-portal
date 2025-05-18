Summary:	Portal frontend service to Flatpak
Summary(pl.UTF-8):	Usługa frontendu portalu dla Flatpaka
Name:		xdg-desktop-portal
Version:	1.20.1
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/flatpak/xdg-desktop-portal/releases
Source0:	https://github.com/flatpak/xdg-desktop-portal/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	1e6218020d0a5c6b0452b50009884bff
URL:		https://github.com/flatpak/xdg-desktop-portal/
BuildRequires:	bubblewrap
BuildRequires:	docutils
BuildRequires:	flatpak-devel >= 1.5.0
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	geoclue2-devel >= 2.5.2
BuildRequires:	gettext-tools >= 0.18.3
BuildRequires:	glib2-devel >= 1:2.72
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.12
BuildRequires:	json-glib-devel
BuildRequires:	libfuse3-devel >= 3.10.0
BuildRequires:	libgudev-devel
BuildRequires:	meson >= 0.60
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 0.2.90
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	python3
BuildRequires:	python3-furo
BuildRequires:	python3-sphinxext.opengraph
BuildRequires:	python3-sphinx_copybutton
BuildRequires:	sphinx-pdg
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dbus
Requires:	flatpak-libs >= 1.5.0
Requires:	geoclue2-libs >= 2.5.2
Requires:	glib2 >= 1:2.72
Requires:	libfuse3 >= 3.10.0
Requires:	pipewire-libs >= 0.2.90
Requires:	systemd-units
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-desktop-portal works by exposing a series of D-Bus interfaces
known as portals under a well-known name
(org.freedesktop.portal.Desktop) and object path
(/org/freedesktop/portal/desktop). The portal interfaces include APIs
for file access, opening URIs, printing and others.

%description -l pl.UTF-8
xdg-desktop-portal działa przez wystawienie szeregu interfejsów D-Bus
zwanych portalami pod dobrze znaną nazwą
(org.freedesktop.portal.Desktop) i ścieżką obiektów
(/org/freedesktop/portal/desktop). Interfejsy portali obejmują API
dostępu do plików, otwieranie URI, drukowanie itd.

%package devel
Summary:	Development files for xdg-desktop-portal
Summary(pl.UTF-8):	Pliki programistyczne xdg-desktop-portal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description devel
Development files for xdg-desktop-portal.

%description devel -l pl.UTF-8
Pliki programistyczne xdg-desktop-portal.

%prep
%setup -q

%build
%meson \
	-Dsystemd-user-unit-dir=%{systemduserunitdir} \
	-Dtests=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_datadir}/xdg-desktop-portal/portals

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS.md README.md %{_vpath_builddir}/doc/html/{_sources,_static,*.html,*.js}
%attr(755,root,root) %{_libexecdir}/xdg-desktop-portal
%attr(755,root,root) %{_libexecdir}/xdg-desktop-portal-rewrite-launchers
%attr(755,root,root) %{_libexecdir}/xdg-desktop-portal-validate-icon
%attr(755,root,root) %{_libexecdir}/xdg-desktop-portal-validate-sound
%attr(755,root,root) %{_libexecdir}/xdg-document-portal
%attr(755,root,root) %{_libexecdir}/xdg-permission-store
%{systemduserunitdir}/xdg-desktop-portal.service
%{systemduserunitdir}/xdg-desktop-portal-rewrite-launchers.service
%{systemduserunitdir}/xdg-document-portal.service
%{systemduserunitdir}/xdg-permission-store.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.host.portal.Registry.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Access.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Account.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.AppChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Background.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Clipboard.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.DynamicLauncher.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Email.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.FileChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.GlobalShortcuts.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Inhibit.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.InputCapture.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Lockdown.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Notification.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.PermissionStore.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Print.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.RemoteDesktop.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Request.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.ScreenCast.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Secret.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Session.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Settings.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Usb.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.Wallpaper.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Account.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Background.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Camera.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Clipboard.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Documents.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.DynamicLauncher.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Email.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.FileChooser.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.FileTransfer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.GameMode.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.GlobalShortcuts.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Inhibit.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.InputCapture.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Location.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.MemoryMonitor.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.NetworkMonitor.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Notification.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.OpenURI.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.PowerProfileMonitor.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Print.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.ProxyResolver.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Realtime.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.RemoteDesktop.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Request.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.ScreenCast.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Secret.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Session.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Settings.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Trash.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Usb.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Wallpaper.xml
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Desktop.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Documents.service
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_mandir}/man5/portals.conf.5*

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/xdg-desktop-portal.pc
