Summary:	DevHelp book: gobject
Summary(pl):	Ksi±¿ka do DevHelp'a o gobject
Name:		devhelp-book-gobject
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gobject-2.0.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about gobject 1.2

%description -l pl
Ksi±¿ka do DevHelp o gobject 1.2

%prep
%setup -q -c gobject-%{version} -n gobject-%{version}

%build
mv -f book gobject-%{version}
mv -f book.devhelp gobject-%{version}.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/gobject-%{version}
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install gobject-%{version}.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install gobject-%{version}/* $RPM_BUILD_ROOT%{_prefix}/books/gobject-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
