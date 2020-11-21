Summary:	Utilities for KDE application development
Name:		kde-dev-utils
Version:	20.11.80
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source10:	kde-dev-utils.rpmlintrc
BuildRequires:	binutils-devel
BuildRequires:	libtool-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(Qt5Designer)
Suggests:	kpartloader = %{EVRD}
Suggests:	kuiviewer = %{EVRD}
# Not being ported to KF5
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
%{_libdir}/qt5/plugins/quithumbnail.so
%{_libdir}/qt5/plugins/kf5/parts/kuiviewerpart.so
%{_datadir}/applications/org.kde.kuiviewer.desktop
%{_datadir}/icons/hicolor/*/apps/kuiviewer.*
%{_datadir}/kservices5/kuiviewer_part.desktop
%{_datadir}/kservices5/designerthumbnail.desktop
%{_datadir}/metainfo/org.kde.kuiviewer.metainfo.xml
%{_datadir}/metainfo/org.kde.kuiviewerpart.metainfo.xml

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kpartloader
%find_lang kuiviewer
