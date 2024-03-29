Summary:	DevHelp book: gobject 2.0
Summary(pl.UTF-8):	Książka do DevHelpa o gobject 2.0
Name:		devhelp-book-gobject
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gobject-2.0.tar.gz
# Source0-md5:	b3b80eb00c7c290b5eeed75040462393
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about gobject 2.0.

%description -l pl.UTF-8
Książka do DevHelpa o gobject 2.0.

%prep
%setup -q -c -n gobject-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gobject-%{version},specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gobject-%{version}.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gobject-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
