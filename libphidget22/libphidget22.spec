Name:           libphidget22
Version:        1.6.20201117
Release:        1%{?dist}
Summary:        Drivers and API for Phidget devices

License:        LGPLv3
URL:            https://www.phidgets.com
Source0:        https://www.phidgets.com/downloads/phidget22/libraries/linux/libphidget22/libphidget22-%{version}.tar.gz

# Needed because Makefile.am is patched
BuildRequires:  libtool
BuildRequires:  autoconf

BuildRequires:  avahi-devel
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  libusb-devel
BuildRequires:  gawk

Requires:       udev
Requires:       avahi-compat-libdns_sd

%description
Phidgets are a set of "plug and play" building blocks for low cost USB 
sensing and control from your PC.  All the USB complexity is taken care 
of by the robust libphidget API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
# These headers are supplied by the avahi-compat-libdns_sd-devel package
# We can get rid of the bundled ones
rm -rf linux/avahi-*
rm -rf include/dns_sd.h

%build
autoreconf -i
%configure --disable-silent-rules --disable-static --enable-zeroconf=avahi --disable-ldconfig --enable-jni
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p -m 0755 $RPM_BUILD_ROOT/lib/udev/rules.d
install -p -m 0644 plat/linux/udev/99-libphidget22.rules $RPM_BUILD_ROOT/lib/udev/rules.d/99-phidgets.rules

%ldconfig_scriptlets

%files
%doc COPYING.LESSER AUTHORS README
%{_libdir}/*.so.*
/lib/udev/rules.d/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Mar  8 2021 Casey Link <casey@outskirtslabs.com> - 1.6.20201117
- Initial build
