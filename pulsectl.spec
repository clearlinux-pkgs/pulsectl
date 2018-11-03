#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pulsectl
Version  : 18.10.6
Release  : 1
URL      : https://files.pythonhosted.org/packages/6e/dd/4e9e91bfeb6e0324bb6ba36ef42f1f08a9ccb6e31cc56bf143763bed8483/pulsectl-18.10.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/dd/4e9e91bfeb6e0324bb6ba36ef42f1f08a9ccb6e31cc56bf143763bed8483/pulsectl-18.10.6.tar.gz
Summary  : Python high-level interface and ctypes-based bindings for PulseAudio (libpulse)
Group    : Development/Tools
License  : MIT
Requires: pulsectl-python = %{version}-%{release}
Requires: pulsectl-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
======================================
        
        Python (3.x and 2.x) high-level interface and ctypes-based bindings for
        PulseAudio_ (libpulse), mostly focused on mixer-like controls and
        introspection-related operations (as opposed to e.g. submitting sound samples to
        play, player-like client).
        
        Originally forked from pulsemixer_ project, which had this code bundled.

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
%setup -q -n pulsectl-18.10.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541254413
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
