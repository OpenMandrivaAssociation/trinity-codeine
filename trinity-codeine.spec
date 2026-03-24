%bcond clang 1
%bcond xine 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg codeine
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		1.0.1
Release:		%{?tde_version:%{tde_version}_}4
Summary:		Simple TDE video player
Group:			Applications/Multimedia
URL:			http://kaffeine.sourceforge.net/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL=ON -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tde-cmake >= %{tde_version}

BuildRequires:	desktop-file-utils

BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# XINE support
%{?with_xine:BuildRequires:  pkgconfig(libxine)}

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
A video player with a different philosophy: simple, uncluttered interface

Features:
- Plays DVDs, VCDs, all video formats supported by Xine
- Bundled with a simple web-page KPart
- Starts quickly


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc COPYING FAQ README.md TODO
%{tde_prefix}/bin/codeine
%{tde_prefix}/share/applications/tde/codeine.desktop
%{tde_prefix}/share/apps/codeine/
%{tde_prefix}/share/apps/konqueror/servicemenus/codeine_play_dvd.desktop
%{tde_prefix}/share/doc/tde/HTML/en/codeine/
%{tde_prefix}/share/icons/hicolor/*/apps/codeine.png
%{tde_prefix}/share/man/man1/codeine.1*
%{tde_prefix}/share/services/codeine_part.desktop
%{tde_prefix}/%{_lib}/trinity/libcodeine.la
%{tde_prefix}/%{_lib}/trinity/libcodeine.so

