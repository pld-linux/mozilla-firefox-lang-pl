Summary:	Polish resources for Mozilla-firefox
Summary(pl):	Polskie pliki jêzykowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-pl
Version:	0.8
Release:	0.3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/mozillapl/firefox-%{version}-pl-PL-langpack.xpi
# Source0-md5:	90f1d5436153d0af34bda5a6e8e3adf1
Source1:	%{name}-installed-chrome.txt
URL:		http://www.firefox.pl/
BuildRequires:	unzip
Requires(post,postun):	mozilla-firefox >= %{version}-1.1
Requires(post,postun):	textutils
Requires:	mozilla-firefox >= %{version}-1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_firefoxdir	%{_libdir}/mozilla-firefox
%define	_chromedir	%{_firefoxdir}/chrome

%description
Polish resources for Mozilla-firefox.

%description -l pl
Polskie pliki jêzykowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_firefoxdir}/{defaults,searchplugins}}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/bin/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/bin/defaults/* $RPM_BUILD_ROOT%{_firefoxdir}/defaults
mv -f $RPM_BUILD_ROOT%{_libdir}/sp/* $RPM_BUILD_ROOT%{_firefoxdir}/searchplugins/

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cd %{_chromedir}
cat firefox-misc-installed-chrome.txt %{name}-installed-chrome.txt >installed-chrome.txt

%postun
umask 022
cd %{_chromedir}
cat firefox-misc-installed-chrome.txt firefox-en-US-installed-chrome.txt >installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/pl-PL.jar
%{_chromedir}/pl-unix.jar
%{_chromedir}/PL.jar
%{_chromedir}/%{name}-installed-chrome.txt
%{_firefoxdir}/defaults/*
%{_firefoxdir}/searchplugins/*
