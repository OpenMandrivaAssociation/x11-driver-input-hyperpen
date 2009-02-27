Name: x11-driver-input-hyperpen
Version: 1.3.0
Release: %mkrel 1
Summary: X.org input driver for HyperPen devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-hyperpen-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
Hyperpen is an X.org input driver for HyperPen devices.

%prep
%setup -q -n xf86-input-hyperpen-%{version}

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/hyperpen_drv.la
%{_libdir}/xorg/modules/input/hyperpen_drv.so
