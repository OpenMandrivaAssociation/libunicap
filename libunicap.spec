%define major	2
%define libname	%mklibname unicap %{major}
%define devname	%mklibname -d unicap

Summary:	Library to access different kinds of ( video ) capture devices 
Name:		libunicap
Version:	0.9.12
Release:	6
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.unicap-imaging.org/
Source0:	http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0:		unicap-0.9.6-v4l1.patch
Patch1:		libunicap-0.9.12-link.patch
Patch2:		libunicap-0.9.12-includes.patch
Patch3:		libunicap-0.9.12-memerrs.patch
Patch4:		libunicap-0.9.12-arraycmp.patch
Patch5:		libunicap-0.9.12-warnings.patch
Patch6:		libunicap-bz641623.patch
Patch7:		libunicap-bz642118.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(libraw1394)
Conflicts:	%{_lib}unicap2 < 0.9.12-2

%description
unicap is a library to access different kinds of ( video ) capture devices. 

%package -n %{libname}
Summary:	Dynamic libraries for Unicap
Group:		System/Libraries
Suggests:	%{name} = %{version}-%{release}

%description -n %{libname}
unicap is a library to access different kinds of ( video ) capture devices. 

%package -n %{devname}
Summary:	Development library, include files for Unicap
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development library and headers file
needed in order to develop applications using unicap.

%prep
%setup -q
%apply_patches
sed -i -e 's/\(SYSFS\|ATTRS\)/ATTRS/g' data/50-euvccam.rules

%build
%configure2_5x --disable-v4l --disable-static
%make

%install
%makeinstall_std
%find_lang unicap

%files -f unicap.lang
%{_sysconfdir}/udev/rules.d/*
%{_libdir}/unicap%{major}

%files -n %{libname}
%{_libdir}/libunicap.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/libunicap
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

