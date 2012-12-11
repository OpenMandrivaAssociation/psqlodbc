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


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 08.04.0100-3mdv2011.0
+ Revision: 614625
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 08.04.0100-2mdv2010.1
+ Revision: 536663
- rebuild

* Mon Nov 23 2009 Funda Wang <fwang@mandriva.org> 08.04.0100-1mdv2010.1
+ Revision: 469246
- New version 08.04.0100

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Oct 11 2008 Olivier Thauvin <nanardon@mandriva.org> 08.03.0300-1mdv2009.1
+ Revision: 291769
- fix group tag
- fix file list to not include debug files
- import psqlodbc



