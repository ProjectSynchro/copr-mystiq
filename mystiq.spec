%define oname MystiQ

Summary:	Audio/Video converter
Name:		mystiq
Version:	20.03.23
Release:	2%{?dist}
License:	GPLv3
Group:		Video
Url:		https://mystiqapp.com/
Source0:	https://github.com/swl-x/MystiQ/archive/v%{version}.tar.gz
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
%endif
%if 0%{?centos} || 0%{?fedora}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquickcontrols
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(x11)
%endif
%if 0%{?centos}


%endif
Requires:	ffmpeg
Requires:	sox

%description
MystiQ is a GUI for FFmpeg, a powerful media converter. 
FFmpeg can read audio and video files in various 
formats and convert them into other formats. 
MystiQ features an intuitive graphical 
interface and a rich set of presets to help you 
convert media files within a few clicks.
Advanced users can also adjust conversion parameters in detail.

%files
%doc LICENSE README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/mystiq.svg
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*.1.xz

#-----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
chmod -x mystiq.desktop icons/mystiq.svg

%if 0%{?is_opensuse}
%build
qmake-qt5 mystiq.pro
make USE_LIBNOTIFY=1 -j$(nproc) VERBOSE=1
%endif

%if 0%{?centos} || 0%{?fedora}
qmake-qt5 mystiq.pro
make USE_LIBNOTIFY=1 -j$(nproc) VERBOSE=1
%endif

%install
%if 0%{?is_opensuse} 
%qmake5_install
%endif

%if 0%{?centos} || 0%{?fedora}
%make_install INSTALL_ROOT=%{buildroot}
%endif

%files
%if 0%{?is_opensuse}
%defattr(-,root,root,-)
%doc LICENSE README.md CONTRIBUTING.md
%{_bindir}/mystiq
%{_datadir}/applications/mystiq.desktop
%{_datadir}/metainfo/mystiq.appdata.xml
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/mystiq.svg
%{_mandir}/man1/mystiq.1.gz
%endif

%if 0%{?centos} || 0%{?fedora}
%doc LICENSE README.md CONTRIBUTING.md
%{_bindir}/mystiq
%{_datadir}/applications/mystiq.desktop
%{_datadir}/metainfo/mystiq.appdata.xml
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/mystiq.svg
%{_mandir}/man1/mystiq.1.gz
%endif


%changelog
* Sat Mar 21 2020 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 20.03.23
- Added stereoscopic filters for 3D video options
- Improved application update notification system
- Improved bugs report option
- Added Hungarian language Pack
- Added Indonesian language Pack
- Improved AppImage File (only GNU/Linux)
- New icons included to the graphical interface

* Tue Feb 18 2020 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 20.02.18
- Added Chinese language Pack
- Added Turkish language Pack
- Added Presets for Youtube
- Added Video Color to Black & White option
- Added Horizontal & Vertical Flip options
- Added metainfo file (only GNU/Linux)
- Fixed Sweden Language Pack
- Changed to Qt 5.14.1 (only Microsoft windows)
- Changed to FFmpeg 4.2.2 (only Microsoft Windows)

* Wed Jan 22 2020 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 20.01.22
- Added Japanese language Pack
- Added Portuguese language Pack
- Added Russian language Pack
- Added Partially added Polish language Pack
- Added MystiQ's manpage (only GNU/Linux)
- Added 32-bit Windows installer (temporarily)
- Missing namespace to demuxing_formats
- Fixed Media Preview in Windows systems
- Fixed Warnings of Qt 5.14
- Fixed Crop math scalar functions
- Fixed Minimum width in mainwindow affecting small screens or tiling window managers
- Fixed Subtitles burning
- Fixed Set Parameters window blank in Windows version
- Changed to QUrl::fromLocalFile to generate the correct file:// url
- Changed background for mystiq logo to dark and light themes
- Removed FFplay support

* Thu Jan 09 2020 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 20.01.09
- Added Swedish language Pack
- Added Italian language Pack
- Updated packages of FFmpeg, FFprobe and FFplay (only for Microsoft Windows)
- Available an installer for Microsoft Windows systems
- Changed version numbering system. Now we use the exact release date as version number.
- Using Qt 5.14 (only Microsoft Windows)
- Cleaned task wizard UI
- It is now possible to reorder items in the initial list of items in taskwizard
- Changed the version number from semantic to date numbers

* Tue Dec 10 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.4.0
- Added French language Pack
- Changed the application icon
- Changed logo to SVG format
- Feature: Replace the preview system with qtmultimedia
- Added Debian based distros build deps
- Avoid pass crop parameters to ffmpeg when not changed the crop on configuration
- Removed more mplayer references.
- Fixed Some bugs on cut & crop dialogs.

* Fri Dec 06 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.3.2
- Addedn new Video Cut Editor
- Added German language pack
- Improved area for video parameter options
- Fixed Continuous integration with TravisCI to generate AppImages packages with each release

* Wed Dec 04 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.3.1
- Fixed UI for better result in dark desktop themes

* Thu Nov 28 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.3.0
- Added donate Option
- Added Continuous Integration with TravisCI 
- Added install target on make, a way to install after build
- Added new option to users, now it's possible report bugs into app
- Explained how to compile the application in Ubuntu 18.04 or earlier, due to the incompatibility of MystiQ with Qt5 <= 5.9
- Added donation in the help menu, a link to send donations to the project
- Changed internal app icons theme

* Tue Nov 05 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.2.0
- Added User Manual
- Added new ffmpeg presets for compression with H265 codec added
- Fixed application update notification system
- Modified toolbar style

* Thu Oct 31 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.1.1
- Cleaning UI

* Fri Oct 11 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.1.0
- Fixed notifications to end a conversion task from a conversion list
- Completed Spanish translation

* Fri Aug 23 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.0.2
- Added Spanish language

* Mon Aug 12 2019 Maikel Llamaret Heredia <llamaret@webmisolutions.com> - 0.0.1
- First stable release.
