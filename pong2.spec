#
# Conditional build:
#%bcond_with	tests		# build with tests
#%bcond_without	tests		# build without tests
#
Summary:	-
#Summary(pl):	-
Name:		pong2
Version:	0.1.0
Release:	0.1
Epoch:		0
License:	GPL v2
Vendor:		Johannes Jordan
Group:		X11/Games
#Icon:		-
Source0:	http://download.berlios.de/pong2/pong2-0.1.0.tar.bz2
# Source0-md5:	651340b5f15544d82912de85d62c7efc
#Source1:	-
# Source1-md5:	-
#Patch0:		%{name}-what.patch
URL:		http://pong2.berlios.de
BuildRequires:	autoconf
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An up till now two player (networked) game inspired by the classical "Pong" from Amiga, which adds another dimension to the playing field. Crazy graphics, fast gameplay, great fun ;)

#%%description -l pl

%prep
%setup -q 

%build
%{__aclocal}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
