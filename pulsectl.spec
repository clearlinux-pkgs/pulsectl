#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pulsectl
Version  : 19.9.5
Release  : 8
URL      : https://files.pythonhosted.org/packages/d8/db/7c0055f9c2ff291c86cbd1f66baa63e8266086e650bb583262dbd642257f/pulsectl-19.9.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/d8/db/7c0055f9c2ff291c86cbd1f66baa63e8266086e650bb583262dbd642257f/pulsectl-19.9.5.tar.gz
Summary  : Python high-level interface and ctypes-based bindings for PulseAudio (libpulse)
Group    : Development/Tools
License  : MIT
Requires: pulsectl-license = %{version}-%{release}
Requires: pulsectl-python = %{version}-%{release}
Requires: pulsectl-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
python-pulse-control (pulsectl module)
======================================
Python (3.x and 2.x) high-level interface and ctypes-based bindings for
PulseAudio_ (libpulse), mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound samples to
play, player-like client).

%package license
Summary: license components for the pulsectl package.
Group: Default

%description license
license components for the pulsectl package.


%package python
Summary: python components for the pulsectl package.
Group: Default
Requires: pulsectl-python3 = %{version}-%{release}

%description python
python components for the pulsectl package.


%package python3
Summary: python3 components for the pulsectl package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pulsectl package.


%prep
%setup -q -n pulsectl-19.9.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569256877
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pulsectl
cp COPYING %{buildroot}/usr/share/package-licenses/pulsectl/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pulsectl/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
