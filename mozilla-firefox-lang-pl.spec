Summary:	Polish resources for Mozilla-firefox
Summary(pl):	Polskie pliki jêzykowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-pl
Version:	0.8
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://beta.firefox.pl/final(2)/firefox-%{version}-pl-PL-langpack.xpi
Nosource:	0
# This file is bad - someone wants to generate him? ;)
Source1:	mozilla-lang-pl-installed-chrome.txt
URL:		http://www.firefox.pl/
BuildRequires:	unzip
Requires(post,postun):	mozilla-firefox = %{version}
Requires(post,postun):	textutils
Requires:	mozilla-firefox = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# %{_libdir}/mozilla/chrome is symlink pointing to the following
%define	_chromedir	%{_datadir}/mozilla-firefox/chrome

%description
Polish resources for Mozilla-firefox.

%description -l pl
Polskie pliki jêzykowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_datadir}/mozilla-firefox/{defaults,searchplugins}}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/bin/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/bin/defaults/* $RPM_BUILD_ROOT%{_datadir}/mozilla-firefox/defaults
mv -f $RPM_BUILD_ROOT%{_libdir}/sp/* $RPM_BUILD_ROOT%{_datadir}/mozilla-firefox/searchplugins/

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun
umask 022
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/pl-PL.jar
%{_chromedir}/pl-unix.jar
%{_chromedir}/PL.jar
%{_chromedir}/mozilla-lang-pl-installed-chrome.txt
%{_datadir}/mozilla-firefox/defaults/*
%{_datadir}/mozilla-firefox/searchplugins/*
