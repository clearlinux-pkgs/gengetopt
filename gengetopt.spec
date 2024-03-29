#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8533F94B6379E538 (wolf@wolfsden.cz)
#
Name     : gengetopt
Version  : 2.23
Release  : 2
URL      : https://ftp.gnu.org/gnu/gengetopt/gengetopt-2.23.tar.xz
Source0  : https://ftp.gnu.org/gnu/gengetopt/gengetopt-2.23.tar.xz
Source1 : https://ftp.gnu.org/gnu/gengetopt/gengetopt-2.23.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gengetopt-bin = %{version}-%{release}
Requires: gengetopt-data = %{version}-%{release}
Requires: gengetopt-license = %{version}-%{release}
Requires: gengetopt-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : help2man
BuildRequires : texinfo
BuildRequires : valgrind

%description
GNU Gengetopt
This program generates a C function that uses /getopt_long/ function to
parse the command line options, to validate them and fills a /struct/ .

%package bin
Summary: bin components for the gengetopt package.
Group: Binaries
Requires: gengetopt-data = %{version}-%{release}
Requires: gengetopt-license = %{version}-%{release}

%description bin
bin components for the gengetopt package.


%package data
Summary: data components for the gengetopt package.
Group: Data

%description data
data components for the gengetopt package.


%package doc
Summary: doc components for the gengetopt package.
Group: Documentation
Requires: gengetopt-man = %{version}-%{release}

%description doc
doc components for the gengetopt package.


%package license
Summary: license components for the gengetopt package.
Group: Default

%description license
license components for the gengetopt package.


%package man
Summary: man components for the gengetopt package.
Group: Default

%description man
man components for the gengetopt package.


%prep
%setup -q -n gengetopt-2.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571709118
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1571709118
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gengetopt
cp COPYING %{buildroot}/usr/share/package-licenses/gengetopt/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/gengetopt/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gengetopt

%files data
%defattr(-,root,root,-)
/usr/share/gengetopt/getopt.c
/usr/share/gengetopt/getopt1.c
/usr/share/gengetopt/gnugetopt.h

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gengetopt/*
%doc /usr/share/info/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gengetopt/COPYING
/usr/share/package-licenses/gengetopt/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gengetopt.1
