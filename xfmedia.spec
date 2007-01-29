#
# Conditional build:
%bcond_without	dbus	# build without dbus support
#
Summary:	Xfmedia - lightweight media player based on the xine engine
Summary(pl):	Xfmedia - lekki odtwarzacz multimedialny oparty na silniku xine
Name:		xfmedia
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://spuriousinterrupt.org/projects/xfmedia/files/%{name}-%{version}.tar.bz2
# Source0-md5:	6eb8bd1f67201f829e0f45e733c02bd5
Patch0:		%{name}-desktop.patch
URL:		http://spuriousinterrupt.org/projects/xfmedia/index.php
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.31}
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libexo-devel >= 0.3.2
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= 4.4.0
BuildRequires:	libxfcegui4-devel >= 4.4.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	taglib-devel
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xine-lib-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	libexo >= 0.3.0
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
Group:		X11/Applications/Multimedia
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--%{?with_dbus:en}%{!?with_dbus:dis}able-dbus \
	--enable-startup-notification \
	--with-taglib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfmedia/plugins/xfmedia-infopipe.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/%{name}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_iconsdir}/hicolor/48x48/apps/*
%{_iconsdir}/hicolor/22x22/actions/*
%{_desktopdir}/*.desktop
%dir %{_datadir}/%{name}
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
%{_pkgconfigdir}/*.pc
