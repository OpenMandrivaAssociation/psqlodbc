%define libname %mklibname psqlodbc

Summary: The official PostgreSQL ODBC Driver
Name: psqlodbc
Version: 08.04.0100
Release: %mkrel 3
Source0: http://wwwmaster.postgresql.org/download/mirrors-ftp/odbc/versions/src/%{name}-%{version}.tar.gz
Patch0: psqlodbc-08.04.0100-fix-build.patch
License: LGPL
Group: Databases
Url: http://www.postgresql.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: unixODBC-devel
BuildRequires: postgresql-devel

%description
The official PostgreSQL ODBC Driver.

%package -n %libname
Group: Databases
Summary: The official PostgreSQL ODBC Driver

%description -n %libname
The official PostgreSQL ODBC Driver.

%prep 
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%_libdir/psqlodbc*
%doc docs
