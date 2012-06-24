Summary:	Mount filesystems in Ruby
Summary(pl):	Montowanie system�w plik�w w j�zyku Ruby
Name:		ruby-mount
Version:	0.2.1
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://theinternetco.net/projects/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	1520432391b21890ebc19206e777ff16
URL:		http://theinternetco.net/projects/ruby/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby interface to the Linux mount(2) call.

%description -l pl
Interfejs j�zyka Ruby do linuksowego wywo�ania mount(2).

%prep
%setup -q

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_sitearchdir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

rdoc -o rdoc ext/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{ruby_archdir}/linux_mount.so
