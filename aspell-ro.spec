%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

#
# NOTE: rpm is unable to package filenames in an enocidng other than the
# the one it is currently using; so this package has to be build with
# an iso-8859-* locale; eg: LC_ALL=fr rpm -be specfile
#

%define src_ver 3.1

%define languageenglazy Romanian
%define languagecode ro
%define lc_ctype ro_RO

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       3.1
Release:       %mkrel 1
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/ro/aspell5-ro-%version.tar.bz2
URL:           http://aspell.net/
License:	   Free
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

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
rm -fr $RPM_BUILD_ROOT
export LC_ALL=fr

%makeinstall_std

#cp doc/README README.%{languagecode}
chmod 644 README Copyright 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Copyright
%{_libdir}/aspell-*/*


