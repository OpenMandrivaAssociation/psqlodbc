%define name psqlodbc
%define version 08.03.0300
%define release %mkrel 1

%define libname %mklibname %name

Summary: The official PostgreSQL ODBC Driver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: LGPL
Group: Databases
Url: http://www.postgresql.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: unixODBC-devel
BuildRequires: postgresql-devel

%description
The official PostgreSQL ODBC Driver.

%package -n %libname
Group: Database
Summary: The official PostgreSQL ODBC Driver

%description -n %libname
The official PostgreSQL ODBC Driver.

%prep 
%setup -q

%build
%configure

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%_libdir/*
%doc docs
