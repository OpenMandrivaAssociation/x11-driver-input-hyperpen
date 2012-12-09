%define gitdate %nil

Name: x11-driver-input-hyperpen
Version: 1.4.1
Release: 3%{?gitdate:.%{gitdate}}
Summary: X.org input driver for HyperPen devices
Group: System/X11
URL: http://xorg.freedesktop.org
%if 0%{?gitdate}
Source0: xf86-input-hyperpen-%{gitdate}.tar.bz2
%else
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-hyperpen-%{version}.tar.bz2
%endif
License: MIT
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Hyperpen is an X.org input driver for HyperPen devices.

%prep
%if 0%{gitdate}
%setup -q -n xf86-input-hyperpen-%{gitdate}
%else
%setup -q -n xf86-input-hyperpen-%{version}
%endif

%build
autoreconf -v --install || exit 1
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/hyperpen_drv.so


%changelog
* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.4.1-2.mdv2012.0
+ Revision: 787177
- Build for x11-server 1.12

* Mon Jan 16 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.4.1-1.
+ Revision: 761729
- 1.4.1
- Remove libtool .la file
- Rebuild with current X server

* Tue Jun 28 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.4.0-1.
+ Revision: 687821
- Updated to 1.4.0

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.3.99.1-1.20110609
+ Revision: 683688
- Updated to latest git snapshot.
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-5
+ Revision: 671125
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.0-4mdv2011.0
+ Revision: 595756
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.0-3mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Jan 19 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3.0-2mdv2010.1
+ Revision: 493609
- Add upstream patch to work with abi 7 (makes package build again)
- Don't autoreconf

* Fri Feb 27 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.0-1mdv2009.1
+ Revision: 345692
- New version 1.3.0

  + Thierry Vignaud <tv@mandriva.org>
    - fix group

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 265855
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194321
- Update to version 1.2.0.

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-7mdv2008.1
+ Revision: 160483
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-6mdv2008.1
+ Revision: 156578
- re-enable rpm debug packages support

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-5mdv2008.1
+ Revision: 155659
- Updated BuildRequires and resubmit package.
- Disable debug package.
  Update BuildRequires.
  Add upstream fixes that should make the driver functional.
  Fix incorrect tag @mandriva to use xorg naming convention.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-input-aiptek-1.1.0@mandriva suggested on upstream
  Tag at git checkout afedccae164668128c6228542585cc27d241b7e6
  There is a tag named hyperpen-1_1_0, but since the only changes up to master
  are .gitignore/.cvsignore edits and change to use macros instead of hardcoded
  version number, the checkout described above was used for the tag
  xf86-input-aiptek-1.1.0@mandriva, that is suggested upstream and follows the
  same pattern of other repositories tags.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-4mdv2008.1
+ Revision: 98632
- minor spec cleanup
- build against xserver 1.4

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2008.0
+ Revision: 75663
- rebuild


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:03:02 (31708)
- fill in summary & descriptions for all input drivers

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 19:59:30 (31594)
- Updated drivers for X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

