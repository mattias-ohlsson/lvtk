%define debug_package %{nil}

Name:           lvtk
Version:        1.2.0
Release:        1%{?dist}
Summary:        C++ Wrapper for LV2

License:        GPLv3+
URL:            https://github.com/lvtk/lvtk
Source0:        https://github.com/lvtk/lvtk/archive/%{version}.tar.gz

BuildRequires:  python2
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconf-pkg-config
BuildRequires:  lv2-devel

%description
This software package contains libraries that wrap the LV2 C API and
extensions into easy to use C++ classes.

%package devel
Summary:        LVTK development files

%description devel
This package holds header files for building programs that link against LVTK.

%prep
%autosetup

# SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Git Tag Created: " + tag)?
sed -i '158d' wscript

%build
python2 waf configure --disable-tools --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir} --debug
python2 waf build

# Remove buildroot from files
sed -i 's|^prefix=.*|prefix=/usr|' build/*.pc

%install
rm -rf $RPM_BUILD_ROOT
python2 waf install

%files devel
%license COPYING
%doc README ChangeLog AUTHORS
%{_includedir}/lvtk-1/lvtk/*.hpp
%{_includedir}/lvtk-1/lvtk/*.h
%{_includedir}/lvtk-1/lvtk/behaviors/*.hpp
%{_includedir}/lvtk-1/lvtk/ext/*.h
%{_includedir}/lvtk-1/lvtk/ext/*.hpp
%{_includedir}/lvtk-1/lvtk/private/*.hpp
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblvtk_plugin1.a
%{_libdir}/liblvtk_ui1.a

%changelog
* Thu Jun 11 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.2.0-1
- Initial build
