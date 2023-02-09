# TODO:
# LOG4CXX_QT_SUPPORT
#
# Conditional build:
%bcond_without	libesmtp	# (E)SMTP support via libesmtp

Summary:	Log4cxx - a port to C++ of the log4j project
Summary(pl.UTF-8):	Log4cxx - port projektu log4j dla C++
Name:		log4cxx
Version:	1.0.0
Release:	2
License:	Apache v2.0
Group:		Libraries
Source0:	http://www.apache.org/dist/logging/log4cxx/%{version}/apache-%{name}-%{version}.tar.gz
# Source0-md5:	2255f30cd968e2c1976081824e435bd5
Patch0:		%{name}-libesmtp.patch
URL:		http://logging.apache.org/log4cxx/
BuildRequires:	apr-devel >= 1
BuildRequires:	apr-util-devel >= 1
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.13
# for tests
BuildRequires:	expat-devel >= 1.95
%{?with_libesmtp:BuildRequires:	libesmtp-devel}
BuildRequires:	libfmt-devel >= 7.1
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	unixODBC-devel
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
Requires:	apr-devel >= 1
Requires:	apr-util-devel >= 1
Requires:	libstdc++-devel >= 6:7
Obsoletes:	log4cxx-static < 1

%description devel
This is the package containing the header files for log4cxx library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki log4cxx.

%prep
%setup -q -n apache-%{name}-%{version}
%patch0 -p1

%build
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	%{!?with_libesmtp:-DHAS_LIBESMTP=OFF}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE NOTICE
%attr(755,root,root) %{_libdir}/liblog4cxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cxx.so.15

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblog4cxx.so
%{_includedir}/%{name}
%{_pkgconfigdir}/liblog4cxx.pc
%{_libdir}/cmake/log4cxx
