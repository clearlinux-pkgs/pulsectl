#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pulsectl
Version  : 19.10.3
Release  : 11
URL      : https://files.pythonhosted.org/packages/df/d6/998acb3b1d1b7a86a54991894932050ecf54a321c7055b110d98fbae0a17/pulsectl-19.10.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/d6/998acb3b1d1b7a86a54991894932050ecf54a321c7055b110d98fbae0a17/pulsectl-19.10.3.tar.gz
Summary  : Python high-level interface and ctypes-based bindings for PulseAudio (libpulse)
Group    : Development/Tools
License  : MIT
Requires: pulsectl-license = %{version}-%{release}
Requires: pulsectl-python = %{version}-%{release}
Requires: pulsectl-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools
BuildRequires : util-linux

%description
======================================
        
        Python (3.x and 2.x) high-level interface and ctypes-based bindings for
        PulseAudio_ (libpulse), mostly focused on mixer-like controls and
        introspection-related operations (as opposed to e.g. submitting sound samples to
        play, player-like client).
        
        Originally forked from pulsemixer_ project, which had this code bundled.

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
%setup -q -n pulsectl-19.10.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571778952
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
cp %{_builddir}/pulsectl-19.10.3/COPYING %{buildroot}/usr/share/package-licenses/pulsectl/cf26bfe991e3b69342541ed04634bf6a19297b70
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pulsectl/cf26bfe991e3b69342541ed04634bf6a19297b70

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
