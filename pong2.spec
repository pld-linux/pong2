# TODO:
#   - add BRs
#   - cleanup
Summary:	-
#Summary(pl):	-
Name:		pong2
Version:	0.1.0
Release:	0.1
Epoch:		0
License:	GPL v2
Vendor:		Johannes Jordan
Group:		X11/Applications/Games
#Icon:		-
Source0:	http://download.berlios.de/pong2/%{name}-%{version}.tar.bz2
# Source0-md5:	651340b5f15544d82912de85d62c7efc
URL:		http://pong2.berlios.de
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An up till now two player (networked) game inspired by the classical
"Pong" from Amiga, which adds another dimension to the playing field.
Crazy graphics, fast gameplay, great fun ;)

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
