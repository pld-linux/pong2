# TODO:
#   - cleanup
Summary:	Pong2 - game inspired by the classical Atari game
Summary(pl):	Pong2 - gra zainspirowana klasyczn± gr± z Atari
Name:		pong2
Version:	0.1.0
Release:	0.1
Epoch:		0
License:	GPL v2
Vendor:		Johannes Jordan
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/pong2/%{name}-%{version}.tar.bz2
# Source0-md5:	651340b5f15544d82912de85d62c7efc
URL:		http://pong2.berlios.de/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An up till now two player (networked) game inspired by the classical
"Pong" from Atari, which adds another dimension to the playing field.
Crazy graphics, fast gameplay, great fun ;)

%description -l pl
Jest to sieciowa gra dla (jak na razie) dwóch graczy zainspirowana
klasyczn± gr± "Pong" z Atari, dodaj±ca dodatkowy wymiar do pola gry.
Zwariowana grafika, szybka akcja, du¿o zabawy ;)

%prep
%setup -q

%build
# ??? aclocal alone can make only troubles
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
