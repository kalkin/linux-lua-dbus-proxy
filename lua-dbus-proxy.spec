%if 0%{?qubes_builder}
%define _sourcedir %(pwd)
%endif

%define mod_name dbus_proxy
%define debug_package %{nil}

Name:           lua-%{mod_name}
Version:        0.8.1
Release:        1%{?dist}
Summary:        D-Bus Lua module built on top of lgi
License:        Apache-2.0
Url:            https://github.com/stefano-m/%{name}
Source:         https://github.com/stefano-m/%{name}/archive/v%{version}.tar.gz
Requires:       lua

%description
dbus_proxy is a Lua module built on top of lgi to offer a simple API to GLib's
GIO GDBusProxy objects. This should make it easier to interact with DBus
interfaces.



%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{lua_libdir}/dbus_proxy/
cp src/dbus_proxy/_bus.lua  $RPM_BUILD_ROOT/%{lua_libdir}/dbus_proxy/
cp src/dbus_proxy/_variant.lua  $RPM_BUILD_ROOT/%{lua_libdir}/dbus_proxy/
cp src/dbus_proxy/init.lua  $RPM_BUILD_ROOT/%{lua_libdir}/dbus_proxy/
cp docs/index.html docs/ldoc.css $RPM_BUILD_ROOT/%{_docdir}/%{name}/

%files
%doc README.md docs/index.html docs/ldoc.css
%{lua_libdir}/dbus_proxy/_bus.lua
%{lua_libdir}/dbus_proxy/_variant.lua
%{lua_libdir}/dbus_proxy/init.lua
