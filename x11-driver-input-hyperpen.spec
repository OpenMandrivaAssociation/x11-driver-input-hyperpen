Summary:	X.org input driver for HyperPen devices
Name:		x11-driver-input-hyperpen
Version:	1.4.1
Release:	21
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-hyperpen-%{version}.tar.bz2
Patch0:		hyperpen-automake-1.13.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Hyperpen is an X.org input driver for HyperPen devices.

%prep
%setup -qn xf86-input-hyperpen-%{version}
%apply_patches
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/hyperpen_drv.so

