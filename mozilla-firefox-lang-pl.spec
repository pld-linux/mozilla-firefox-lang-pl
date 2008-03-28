# TODO:
#  - do something with *.rdf file, there if file conflict with other lang packages
#
%define		_lang		pl
Summary:	Polish resources for Mozilla-firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-%{_lang}
Version:	2.0.0.13
Release:	2
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications/Networking
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/%{_lang}.xpi
# Source0-md5:	eb805bb48fd12771609a5360481f7f59
Source1:	pl-PL.manifest
URL:		http://www.firefox.pl/
BuildRequires:	unzip
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_datadir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
Polish resources for Mozilla-firefox.

%description -l pl.UTF-8
Polskie pliki językowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_firefoxdir}/{defaults/profile,searchplugins}}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/pl.jar $RPM_BUILD_ROOT%{_chromedir}/pl-PL.jar
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_firefoxdir}/defaults/profile

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/pl-PL.jar
%{_chromedir}/pl-PL.manifest
%{_firefoxdir}/defaults/profile/*.rdf
