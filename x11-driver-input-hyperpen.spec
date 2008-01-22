Name: x11-driver-input-hyperpen
Version: 1.1.0
Release: %mkrel 6
Summary: X.org input driver for HyperPen devices
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-input-hyperpen-1.1.0@mandriva suggested on upstream
# Tag at git checkout dc2d398f11b6ca19dd0024e88dccfa3c6f73341d
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-hyperpen xorg/drivers/xf86-input-hyperpen
# cd xorg/drivers/xf86-input/hyperpen
# git-archive --format=tar --prefix=xf86-input-hyperpen-1.1.0/ xf86-input-hyperpen-1.1.0@mandriva | bzip2 -9 > xf86-input-hyperpen-1.1.0.tar.bz2
########################################################################
Source0: xf86-input-hyperpen-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-hyperpen-1.1.0@mandriva..origin/mandriva+gpl
Patch1: 0001-Don-t-check-if-the-device-is-a-core-device-or-not.patch
Patch2: 0002-Make-the-hyperpen-driver-actually-report-sensible-pr.patch
Patch3: 0003-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
Hyperpen is an X.org input driver for HyperPen devices.

%prep
%setup -q -n xf86-input-hyperpen-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/hyperpen_drv.so
