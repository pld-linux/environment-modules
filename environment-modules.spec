#
Summary:	Provides dynamic modification of a user's environment
Name:		environment-modules
Version:	3.2.7b
Release:	0.01
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/modules/modules-%{version}.tar.bz2
# Source0-md5:	3ebba50a1f79e63aa9e2189e9e6c7952
Source1:	modules.sh
Patch0:		%{name}-bindir.patch
URL:		http://modules.sourceforge.net/
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Environment Modules package provides for the dynamic modification
of a user's environment via modulefiles.

Each modulefile contains the information needed to configure the shell
for an application. Once the Modules package is initialized, the
environment can be modified on a per-module basis using the module
command which interprets modulefiles. Typically modulefiles instruct
the module command to alter or set shell environment variables such as
PATH, MANPATH, etc. modulefiles may be shared by many users on a
system and users may have their own collection to supplement or
replace the shared modulefiles.

Modules can be loaded and unloaded dynamically and atomically, in an
clean fashion. All popular shells are supported, including bash, ksh,
zsh, sh, csh, tcsh, as well as some scripting languages such as perl.

Modules are useful in managing different versions of applications.
Modules can also be bundled into metamodules that will load an entire
suite of different applications.


%prep
%setup -q -n modules-3.2.7
%patch0 -p1

%build
%configure \
	--disable-versioning \
	--prefix=%{_datadir} \
	--exec-prefix=%{_datadir}/Modules \
	--with-module-path=%{_sysconfdir}/modulefiles

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -D %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/shrc.d/modules.sh
ln -s %{_datadir}/Modules/init/csh $RPM_BUILD_ROOT%{_sysconfdir}/shrc.d/modules.csh
install -d $RPM_BUILD_ROOT%{_sysconfdir}/modulefiles

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/modulecmd
%dir %{_sysconfdir}/modulefiles
%{_sysconfdir}/shrc.d/modules.*
%{_datadir}/Modules
%{_mandir}/man1/module.1.*
%{_mandir}/man4/modulefile.4.*

%doc ChangeLog INSTALL NEWS README TODO
