#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Utilities for KDE application development
Name:		plasma6-kde-dev-utils
Version:	24.02.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/kde-dev-utils/-/archive/%{gitbranch}/kde-dev-utils-%{gitbranchd}.tar.bz2#/kde-dev-utils-%{git}.tar.bz2
%else
Source0:	https://invent.kde.org/sdk/kde-dev-utils/-/archive/master/kde-dev-utils-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/kde-dev-utils/-/archive/%{gitbranch}/kde-dev-utils-%{gitbranchd}.tar.bz2#/kde-dev-utils-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kde-dev-utils-%{version}.tar.xz
%endif
%endif
#Source10:	kde-dev-utils.rpmlintrc
BuildRequires:	binutils-devel
BuildRequires:	libtool-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6UiTools)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qttools-designer
Suggests:	kpartloader = %{EVRD}
Suggests:	kuiviewer = %{EVRD}
# Not being ported to KF6
Obsoletes:	kprofilemethod < %{EVRD}
Obsoletes:	kstartperf < %{EVRD}
Obsoletes:	kmtrace < %{EVRD}
Obsoletes:	%mklibname ktrace 4
Obsoletes:	%mklibname ktrace -d

%description
Utilities for KDE application development:
 - kmtrace: memory allocation debugging tool for KDE
 - kpartloader: test application for KParts
 - kprofilemethod: helper macros for profiling using QTime
 - kstartperf: startup time measurement tool for KDE applications
 - kuiviewer: UI files viewer for KDE

%files

#----------------------------------------------------------------------------

%package -n kpartloader
Summary:	Test application for KParts
Group:		Graphical desktop/KDE
Conflicts:	kdesdk4-core < 1:4.11.0

%description -n kpartloader
Test application for KParts.

%files -n kpartloader -f kpartloader.lang
%{_bindir}/kpartloader

#----------------------------------------------------------------------------

%package -n kuiviewer
Summary:	UI files viewer for KDE
Group:		Graphical desktop/KDE

%description -n kuiviewer
Displays Qt Designer UI files.

%files -n kuiviewer -f kuiviewer.lang
%{_bindir}/kuiviewer
%{_libdir}/qt6/plugins/kf6/thumbcreator/quithumbnail.so
%{_libdir}/qt6/plugins/kf6/parts/kuiviewerpart.so
%{_datadir}/applications/org.kde.kuiviewer.desktop
%{_datadir}/icons/hicolor/*/apps/kuiviewer.*
#{_datadir}/kservices6/kuiviewer_part.desktop
#{_datadir}/kservices6/designerthumbnail.desktop
%{_datadir}/metainfo/org.kde.kuiviewer.metainfo.xml
%{_datadir}/metainfo/org.kde.kuiviewerpart.metainfo.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kde-dev-utils-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kpartloader
%find_lang kuiviewer
