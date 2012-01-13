Summary:	Pong2 - game inspired by the classical Atari game
Summary(pl.UTF-8):	Pong2 - gra zainspirowana klasyczną grą z Atari
Name:		pong2
Version:	0.1.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/pong2/%{name}-%{version}.tar.bz2
# Source0-md5:	b27c827a060c1d0aebb4d0df825fcada
URL:		http://pong2.berlios.de/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An up till now two player (networked) game inspired by the classical
"Pong" from Atari, which adds another dimension to the playing field.
Crazy graphics, fast gameplay, great fun ;)

%description -l pl.UTF-8
Jest to sieciowa gra dla (jak na razie) dwóch graczy zainspirowana
klasyczną grą "Pong" z Atari, dodająca dodatkowy wymiar do pola gry.
Zwariowana grafika, szybka akcja, dużo zabawy ;)

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
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
