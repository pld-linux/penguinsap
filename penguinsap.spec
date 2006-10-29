Summary:	SAP tunes player for Linux text terminal
Summary(pl):	Odtwarzacz melodii SAP dla linuksowego terminala tekstowego
Name:		penguinsap
Version:	0.1
Release:	1
License:	Freeware
Group:		Applications/Sound
Source0:	http://asma.atari.org/bin/pengiunsap-%{version}.tar.bz2
# Source0-md5:	800f818d3ef1b93346b07a5861bb1e17
URL:		http://asma.atari.org/
BuildRequires:	libsap-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SAP tunes player for Linux text terminal.

%description -l pl
Odtwarzacz melodii SAP dla linuksowego terminala tekstowego.

%prep
%setup -q

rm -f sapLib.h
ln -sf /usr/include/libsap.h sapLib.h

%build
%{__cxx} %{rpmldflags} %{rpmcxxflags} -o penguinsap main.cpp -lsap

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install penguinsap $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/penguinsap
