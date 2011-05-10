%define lib_major	2
%define lib_name	%mklibname unicap %{lib_major}
%define develname	%mklibname -d unicap

Summary: Library to access different kinds of ( video ) capture devices 
Name: libunicap
Version: 0.9.12
Release: %mkrel 1
Source0: http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0: unicap-0.9.6-v4l1.patch
Patch1: libunicap-0.9.12-link.patch
Patch2: libunicap-0.9.12-includes.patch
Patch3: libunicap-0.9.12-memerrs.patch
Patch4: libunicap-0.9.12-arraycmp.patch
Patch5: libunicap-0.9.12-warnings.patch
Patch6: libunicap-bz641623.patch
Patch7: libunicap-bz642118.patch
License: GPLv2+
Group: System/Libraries
Url: http://www.unicap-imaging.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libraw1394-devel
BuildRequires: intltool
Conflicts: %{_lib}unicap2 < 0.9.12

%description
unicap is a library to access different kinds of ( video ) capture devices. 

%package -n %{lib_name}
Summary:	Dynamic libraries for Unicap
Group:		System/Libraries
Requires:	%{name} = %{version}

%description -n %{lib_name}
unicap is a library to access different kinds of ( video ) capture devices. 

%package -n %{develname}
Summary:	Static libraries, include files for Unicap
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Obsoletes:	%{lib_name}-devel < %{version}
Obsoletes:	%{name}-devel < %{version}

%description -n %{develname}
Static library and headers file
needed in order to develop applications using unicap.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

sed -i -e 's/\(SYSFS\|ATTRS\)/ATTRS/g' data/50-euvccam.rules

%build
%configure2_5x --disable-v4l --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/unicap%{lib_major}/{backends,cpi}/*.{la,a} 

%find_lang unicap

%clean
rm -rf $RPM_BUILD_ROOT

%files -f unicap.lang
%defattr(-,root,root)
%{_sysconfdir}/udev/rules.d/*
%{_libdir}/unicap%{lib_major}

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.%{lib_major}*

%files -n %{develname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/libunicap
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.la
