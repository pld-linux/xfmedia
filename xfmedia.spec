#
%bcond_without	dbus
#
Summary:	Xfmedia - lightweight media player based on the xine engine
Summary(pl):	Xfmedia - lekki odtwarzacz multimedialny oparty na silniku xine
Name:		xfmedia
Version:	0.9.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://spuriousinterrupt.org/projects/xfmedia/files/%{name}-%{version}.tar.bz2
# Source0-md5:	5ab3d25703d16ab4074dc63e677d0367
Source1:	%{name}.desktop
URL:		http://spuriousinterrupt.org/projects/xfmedia/index.php
#BuildRequires:	autoconf >= 2.50
#BuildRequires:	automake >= 1:1.8
%{?with_dbus:BuildRequires:	dbus-devel >= 0.23}
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libexo-devel >= 0.3.0
BuildRequires:	libxfcegui4-devel >= 4.2.0
BuildRequires:	libxfce4util-devel >= 4.2.0
BuildRequires:	xine-lib-devel
Requires:	gtk+2 >= 2:2.4.0
Requires:	libexo >= 0.3.0
Requires:	libxfcegui4 >= 4.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfmedia is a lightweight media player based on the xine engine. The
GTK+ GUI focuses on playing and managing audio files, but, being based
on xine, supports video as well.

%description -l pl
Xfmedia jest lekkim odtwarzaczem multimedialnym opartym o silnik xine.
Interfejs GTK+ skupia siê na zarz±dzaniu i odtwarzaniu plików audio,
ale, jako ¿e jest oparty na xine, obs³uguje równie¿ pliki wideo.

%package plugins
Summary:	Xfmedia plugins
Summary(pl):	Wtyczki dla Xfmedia
Group:		X11/Application/Multimedia
Requires:	%{name} = %{version}-%{release}

%description plugins
Xfmedia plugins:
- infopipe

%description plugins -l pl
Wtyczki dla Xfmedia:
- infopipe

%package devel
Summary:	Header files for Xfmedia
Summary(pl):	Pliki nag³ówkowe Xfmedia
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Xfmedia - header files.

%description devel -l pl
Xfmedia - pliki nag³ówkowe.

%prep
%setup -q

%build
#%%{__aclocal} -I m4
#%%{__autoconf}
#%%{__automake}
%configure \
	--disable-static \
	%{!?with_dbus: --disable-dbus}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%config(noreplace) %verify(not md5 mtime size) /etc/xdg/%{name}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_iconsdir}/hicolor/48x48/apps/*
%{_iconsdir}/hicolor/22x22/actions/*
%{_desktopdir}/*
%dir %{_datadir}/%{name}/doc
%{_datadir}/%{name}/doc/xfce.css
%dir %{_datadir}/%{name}/doc/C/
%{_datadir}/%{name}/doc/C/*

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*
