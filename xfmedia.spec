#
# TODO:
# - better description and summary

Summary:	Xfmedia - lightweight media player based on the xine engine
Summary(pl):	Xfmedia - lekki odtwarzacz multimedialny oparty na xine
Name:		xfmedia
Version:	0.6.0
Release:	0.3
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://spuriousinterrupt.org/projects/xfmedia/files/%{name}-%{version}.tar.bz2
# Source0-md5:	da83e30744b47fc034731fb160197470
Source1:	%{name}.desktop
URL:		http://spuriousinterrupt.org/projects/xfmedia/index.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	libxfcegui4 >= 4.2.0
BuildRequires:	xine-lib-devel
Requires:	gtk+2 >= 2.4
Requires:	libxfcegui4 >= 4.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfmedia is a lightweight media player based on the xine engine. The
GTK+ GUI focuses on playing and managing audio files, but, being based
on xine, supports video as well.

%description -l pl
Xfmedia jest lekkim odtwarzaczem multimedialnym opartym o silnik xine.
Interfejs GTK+ skupia siê na zarz±dzaniu i odtwarzaniu plików audio,
ale, bêd±c opartym na xine, wspiera równie¿ pliki wideo.

%package plugins
Summary:	Xfmedia plugins
Summary(pl):	Wtyczki Xfmedia
Group:		X11/Application/Multimedia
Requires:	%{name} >= %{version}-%{release}

%description plugins
Xfmedia plugins.

%description plugins -l pl
Wtyczki Xfmedia.

%package devel
Summary:	Header files for Xfmedia
Summary(pl):	Pliki nag³ówkowe Xfmedia
Group:		X11/Development/Libraries
Requires:	%{name} >= %{version}-%{release}

%description devel
Xfmedia header files.

%description devel -l pl
PLiki nag³ówkowe Xfmedia.

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
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/%{name}/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/22x22/actions/*
%{_desktopdir}/*

%files plugins
%defattr(644,root,root,755)
%{_libdir}/%{name}/plugins/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*
