Summary:	Log4cxx - a port to C++ of the log4j project
Summary(pl.UTF-8):	Log4cxx - port projektu log4j dla C++
Name:		log4cxx
Version:	0.9.7
Release:	0.2
License:	Apache
Group:		Libraries
Source0:	http://www.apache.org/dist/logging/log4cxx/%{name}-%{version}.tar.gz
# Source0-md5:	fd09abc90b8c0c8af1d5146a75590792
URL:		http://logging.apache.org/log4cxx/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4cxx is C++ port of Log4j. Log4cxx attempts to mimic log4j usage as
much as the language will allow and to be compatible with log4j
configuration and output formats.

%description -l pl.UTF-8
Log4cxx jest portem Log4j dla C++. Log4cxx próbuje naśladować
użytkowanie log4j tak bardzo na ile pozwala na to język oraz próbuje
być kompatybilnym z plikami konfiguracyjnymi i formatami wyjściowymi
log4j.

%package devel
Summary:	Header files for log4cxx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki log4cxx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for log4cxx library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki log4cxx.

%package static
Summary:	Static log4cxx library
Summary(pl.UTF-8):	Statyczna biblioteka log4cxx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static log4cxx library.

%description static -l pl.UTF-8
Statyczna biblioteka log4cxx.

%prep
%setup -q

%build
cp %{_datadir}/aclocal/libtool.m4 aclocal.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/liblog4cxx.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblog4cxx.so
%{_libdir}/liblog4cxx.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/liblog4cxx.a
