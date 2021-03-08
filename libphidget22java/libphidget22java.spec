Name:           libphidget22java
Version:        1.6.20201117
Release:        1%{?dist}
Summary:        Java bindings for Phidget devices

License:        LGPLv3
URL:            http://www.phidgets.com
Source0:        https://www.phidgets.com/downloads/phidget22/libraries/linux/libphidget22java/libphidget22java-%{version}.tar.gz
Patch0:         libphidget22java.javadir.patch

BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  libphidget22-devel

Requires:       libphidget22
Requires:       java-headless >= 1:1.6.0
Requires:       jpackage-utils

%description
The %{name}-java package contains java bindings for the 
libphidget22 API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .javadir

%build
%configure --disable-silent-rules --disable-static --disable-ldconfig
make %{?_smp_mflags}
make phidget22.jar

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets


%files
%doc COPYING.LESSER AUTHORS README
%{_libdir}/*.so.*
%{_jnidir}/phidget22.jar

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Mar  8 2021 Casey Link <casey@outskirtslabs.com> - 1.6.20201117
- Initial build
