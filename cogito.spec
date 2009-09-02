Summary:	Cogito scm with git core
Name:		cogito
Version:	0.18.2
Release:	%mkrel 5
Source0:	http://www.kernel.org/pub/software/scm/cogito/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Development/Other
Url:		http://www.kernel.org/pub/software/scm/cogito/
BuildRequires:	openssl-devel
BuildRequires:  curl-devel
BuildRequires:  zlib-devel
Requires: 	rsync
Requires:       mktemp >= 1.5
Requires:       diffutils
Requires:       git-core
BuildArch:      noarch
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Cogito is a version control system layered on top of the git tree history
storage system. It aims at seamless user interface and ease of use, providing
generally smoother user experience than the "raw" Core GIT itself and indeed
many other version control systems.

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} libdir=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/cg*
#%{_bindir}/commit-id
#%{_bindir}/parent-id
#%{_bindir}/tree-id
%{_datadir}/%{name}
%doc README VERSION COPYING 



