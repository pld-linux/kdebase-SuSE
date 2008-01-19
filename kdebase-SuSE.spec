Summary:	SuSE KDE Extensions
Summary(pl.UTF-8):	Rozszerzenia SuSE dla KDE
Name:		kdebase-SuSE
Version:	10.3
Release:	0.152.3
License:	GPL v2+
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	e60cbfd384f2bb21c7446eb780aa63ad
# to get it building on AC
Patch0:		%{name}-rpmsense.patch
BuildRequires:	ImageMagick-devel
BuildRequires:	db-devel
BuildRequires:	dbus-qt-devel
BuildRequires:	hal-devel
BuildRequires:	hwinfo-devel
BuildRequires:	kdebase-devel
BuildRequires:	rpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the standard SuSE desktop and menu extensions
for the Kpanel.

%description -l pl.UTF-8
Ten pakiet zawiera standardowe rozszerzenia SuSE do pulpitu i menu
dla Kpanelu.

%package -n kde-kio-sysinfo
Summary:	System Information KIO-Slave
Summary(pl.UTF-8):	KIO-Slave z informacjami systemowymi
Group:		X11/Applications

%description -n kde-kio-sysinfo
This package contains a KDE KIO-Slave showing system information.

%description -n kde-kio-sysinfo -l pl.UTF-8
Ten pakiet zawiera moduł KDE KIO-Slave pokazujący informacje
systemowe.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#cp -a config-files/* $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/krpmview
cp -a meta/* $RPM_BUILD_ROOT%{_datadir}/apps/krpmview

rm -f *.lang
%find_lang SUSEgreeter
%find_lang suseplugger
%find_lang kfiledialog
%find_lang krpmview
%find_lang susetranslations
%find_lang kryptomedia
cat *.lang > suse.lang

%find_lang kio_sysinfo

# remove empty language catalogs (= 1 message only)
find $RPM_BUILD_ROOT%{_datadir}/locale -type f -name '*.mo' | xargs file | egrep ', 1 messages$' | cut -d: -f1 | xargs rm -vf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f suse.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/SUSEgreeter
%attr(755,root,root) %{_bindir}/floppy_configure.sh
%attr(755,root,root) %{_bindir}/kfiledialog
%attr(755,root,root) %{_bindir}/kryptomedia
%attr(755,root,root) %{_bindir}/ksplashx
%attr(755,root,root) %{_bindir}/ksplashx_scale
%attr(755,root,root) %{_bindir}/suseplugger
%attr(755,root,root) %{_bindir}/update_fstab.sh

# Qt KDE integration
%{_libdir}/kde3/kded_kdeintegration.la
%attr(755,root,root) %{_libdir}/kde3/kded_kdeintegration.so
%dir %{_libdir}/kde3/plugins/integration
%{_libdir}/kde3/plugins/integration/libqtkde.la
%attr(755,root,root) %{_libdir}/kde3/plugins/integration/libqtkde.so
%{_datadir}/services/kded/kdeintegration.desktop

%{_libdir}/kde3/libkrpmview.la
%attr(755,root,root) %{_libdir}/kde3/libkrpmview.so
%{_libdir}/kde3/suseplugger.la
%attr(755,root,root) %{_libdir}/kde3/suseplugger.so
%{_libdir}/libkdeinit_suseplugger.la
%attr(755,root,root) %{_libdir}/libkdeinit_suseplugger.so
%{_desktopdir}/kde/SUSEgreeter.desktop
%{_desktopdir}/kde/konqfilemgr_rpm.desktop
%{_datadir}/apps/SUSEgreeter
%{_datadir}/apps/ksplash/Themes/ksplashx-suse
%{_datadir}/apps/suseplugger
%{_datadir}/autostart/SUSEgreeter.desktop
%{_datadir}/autostart/suseplugger.desktop
%{_datadir}/config/susepluggerrc
%{_iconsdir}/crystalsvg/*/apps/SuSEconf.png
%{_iconsdir}/crystalsvg/*/apps/SuSEgo.png
%{_iconsdir}/crystalsvg/*/apps/SuSElogo1.png
%{_iconsdir}/crystalsvg/*/apps/SuSEmenu.png
%{_iconsdir}/crystalsvg/*/apps/gnome/suse.png
%{_iconsdir}/crystalsvg/*/apps/openoffice.png
%{_iconsdir}/crystalsvg/*/apps/suse_doc.png
%{_iconsdir}/crystalsvg/*/apps/suse_link.png
%{_iconsdir}/crystalsvg/*/apps/suse_portal.png
%{_iconsdir}/crystalsvg/*/apps/suse_sdb.png
%{_iconsdir}/crystalsvg/*/apps/suse_tour.png
%{_iconsdir}/crystalsvg/*/apps/susehelpcenter.png
%{_iconsdir}/crystalsvg/*/apps/yast.png
%{_iconsdir}/crystalsvg/scalable/apps/SuSEgo.svgz
%{_iconsdir}/crystalsvg/scalable/apps/SuSEmenu.svgz
%{_iconsdir}/hicolor/*/apps/kryptomedia.png
%{_iconsdir}/locolor/*/apps/krpmview.png
%{_datadir}/services/krpmview.desktop

%if 0
%dir %{_sysconfdir}%{_datadir}
%dir %{_sysconfdir}%{_datadir}/config
%config %{_sysconfdir}%{_datadir}/config/ipv6blacklist
%{_sysconfdir}%{_datadir}/apps
%{_sysconfdir}%{_desktopdir}
%{_sysconfdir}%{_docdir}/
%{_sysconfdir}%{_datadir}/mimelnk
%exclude %{_datadir}/mimelnk/application/x-sysinfo.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_iconsdir}/*
%config(noreplace) %{_sysconfdir}%{_datadir}/config/*rc
/opt/kde3/bin/*
/opt/kde3/env
%{_datadir}/wallpapers
%{_datadir}/autostart/*.desktop
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/suseplugger
%{_datadir}/apps/SUSEgreeter
%{_datadir}/apps/kthememanager
%{_datadir}/apps/kicker/wallpapers/SuSE.png
%{_datadir}/apps/kdm
%{_datadir}/apps/ksplash
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/ftp/opensuse_ftp.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/ftp/suse_ftp.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/novell_linux.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/opensuse.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/remote/web/suse_linux.desktop
%{_datadir}/apps/krpmview
%{_datadir}/applnk/.hidden/kdeymp.desktop
%{_datadir}/applnk/.hidden/kdeymu.desktop
%{_docdir}
%{_datadir}/config/SuSE
%{_datadir}/mimelnk/text/x-suse-ymp.desktop
%{_datadir}/mimelnk/text/x-suse-ymu.desktop
%config(noreplace) /etc/X11/kstylerc
%config(noreplace) %{_datadir}/config/*rc
%config(noreplace) %{_datadir}/config/kdeglobals
/opt/kde3/%_lib/libkdeinit_suse*
%{_libdir}/kde3/suse*
%{_libdir}/kde3/libkrpmview.*
%{_datadir}/services/krpmview.desktop
%config(noreplace) /etc/X11/qt_gtk_fnt2fntrc
%{_datadir}/apps/konqueror/servicemenus/*.desktop
/var/adm/fillup-templates/sysconfig.*-kdebase3-SuSE
/var/lib/kde-profiles
%endif

%files -n kde-kio-sysinfo
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_sysinfo.la
%attr(755,root,root) %{_libdir}/kde3/kio_sysinfo.so
%{_libdir}/kde3/libksysinfopart.la
%attr(755,root,root) %{_libdir}/kde3/libksysinfopart.so
%{_desktopdir}/kde/kfmclient_sysinfo.desktop
%{_datadir}/apps/sysinfo
%{_datadir}/mimelnk/application/x-sysinfo.desktop
%{_datadir}/services/ksysinfopart.desktop
%{_datadir}/services/sysinfo.protocol
