%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

#
# NOTE: rpm is unable to package filenames in an enocidng other than the
# the one it is currently using; so this package has to be build with
# an iso-8859-* locale; eg: LC_ALL=fr rpm -be specfile
#

%define src_ver 3.3-2

%define languageenglazy Romanian
%define languagecode ro
%define lc_ctype ro_RO

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       3.3.2
Release:       1
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/ro/aspell5-ro-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   Free

BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50
BuildRequires: locales-fr

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}
Provides:      spell-%{languagecode} >= 0.50.2-5mdk
Obsoletes:	   ispell-%{languagecode}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n aspell5-ro-%{src_ver}

%build
export LC_ALL=fr
# don't use configure macro
./configure

%make

%install
export LC_ALL=fr

%makeinstall_std

#cp doc/README README.%{languagecode}
chmod 644 README Copyright 

%files
%doc README Copyright
%{_libdir}/aspell-*/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1-6mdv2011.0
+ Revision: 662863
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1-5mdv2011.0
+ Revision: 603456
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1-4mdv2010.1
+ Revision: 518957
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3.1-3mdv2010.0
+ Revision: 413099
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 3.1-2mdv2009.1
+ Revision: 350109
- 2009.1 rebuild

* Sun Jun 15 2008 Funda Wang <fwang@mandriva.org> 3.1-1mdv2009.0
+ Revision: 219199
- New version 3.1

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.50.2-9mdv2008.1
+ Revision: 182630
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-8mdv2008.1
+ Revision: 148846
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-7mdv2007.0
+ Revision: 124102
- rebuilt due to bs fjukiness
- Import aspell-ro

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-6mdv2007.1
- use the mkrel macro
- disable debug packages

* Wed Sep 28 2005 Laurent MONTEL <lmontel@mandriva.com> 0.50.2-5mdk
- Fix provides

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.2-4mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-3mdk
- allow build on ia64

