Summary:	Utilities for KDE application development
Name:		kde-dev-utils
Version:	4.11.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	binutils-devel
BuildRequires:	libtool-devel
BuildRequires:	kdelibs4-devel
Suggests:	kmtrace = %{EVRD}
Suggests:	kpartloader = %{EVRD}
Suggests:	kprofilemethod = %{EVRD}
Suggests:	kstartperf = %{EVRD}
Suggests:	kuiviewer = %{EVRD}

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

%files -n kpartloader
%{_kde_bindir}/kpartloader
%{_kde_appsdir}/kpartloader

#----------------------------------------------------------------------------

%package -n kprofilemethod
Summary:	Helper macros for profiling using QTime
Group:		Development/KDE and Qt
Conflicts:	kdesdk4-devel < 1:4.11.0

%description -n kprofilemethod
Helper macros for profiling using QTime.

%files -n kprofilemethod
%doc kprofilemethod/README
%{_kde_includedir}/kprofilemethod.h

#----------------------------------------------------------------------------

%package -n kstartperf
Summary:	Startup time measurement tool for KDE applications
Group:		Graphical desktop/KDE
Conflicts:	kdesdk4-core < 1:4.11.0
Conflicts:	kdesdk4-scripts < 1:4.11.0

%description -n kstartperf
Startup time measurement tool for KDE applications.

%files -n kstartperf
%{_kde_bindir}/kstartperf
%{_kde_libdir}/kde4/kstartperf.so

#----------------------------------------------------------------------------

%package -n kuiviewer
Summary:	UI files viewer for KDE
Group:		Graphical desktop/KDE

%description -n kuiviewer
Displays Qt Designer UI files.

%files -n kuiviewer
%{_kde_bindir}/kuiviewer
%{_kde_libdir}/kde4/quithumbnail.so
%{_kde_libdir}/kde4/kuiviewerpart.so
%{_kde_applicationsdir}/kuiviewer.desktop
%{_kde_appsdir}/kuiviewer
%{_kde_appsdir}/kuiviewerpart
%{_kde_iconsdir}/hicolor/*/apps/kuiviewer.png
%{_kde_services}/kuiviewer_part.desktop
%{_kde_services}/designerthumbnail.desktop

#----------------------------------------------------------------------------

%package -n kmtrace
Summary:	Memory allocation debugging tool for KDE
Group:		Graphical desktop/KDE
Conflicts:	kdesdk4-scripts < 1:4.11.0

%description -n kmtrace
Memory allocation debugging tool for KDE.

%files -n kmtrace
%{_kde_bindir}/kmtrace
%{_kde_bindir}/demangle
%{_kde_bindir}/kminspector
%{_kde_bindir}/kmmatch
%{_kde_appsdir}/kmtrace
%{_kde_mandir}/man1/demangle.1.*

#----------------------------------------------------------------------------

%define ktrace_major 4
%define libktrace %mklibname ktrace %{ktrace_major}

%package -n %{libktrace}
Summary:	Shared library for kmtrace
Group:		System/Libraries

%description -n %{libktrace}
Shared library for kmtrace.

%files -n %{libktrace}
%{_kde_libdir}/libktrace.so.%{ktrace_major}*

#----------------------------------------------------------------------------

%define devktrace %mklibname ktrace -d

%package -n %{devktrace}
Summary:	Development files for kmtrace
Group:		Development/KDE and Qt
Requires:	%{libktrace} = %{EVRD}
Provides:	kmtrace-devel = %{EVRD}
Conflicts:	kdesdk4-devel < 1:4.11.0

%description -n %{devktrace}
This package includes the header files you will need to compile applications
based on kmtrace libraries.

%files -n %{devktrace}
%{_kde_includedir}/ktrace.h
%{_kde_libdir}/libktrace.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
