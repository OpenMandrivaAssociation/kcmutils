%define major 5
%define libname %mklibname KF5KCMUtils %{major}
%define devname %mklibname KF5KCMUtils -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kcmutils
Version:	5.52.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 framework for writing System Settings modules
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(ECM)
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 framework for writing System Settings modules.

%package -n %{libname}
Summary: The KDE Frameworks 5 framework for writing System Settings modules
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 framework for writing System Settings modules.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_datadir}/kservicetypes5/kcmodule*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/*
%{_libdir}/cmake/KF5KCMUtils
