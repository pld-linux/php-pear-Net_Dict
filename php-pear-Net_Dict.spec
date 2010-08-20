%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Dict
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - interface to the DICT protocol
Summary(pl.UTF-8):	%{_pearname} - interfejs do protokołu DICT
Name:		php-pear-%{_pearname}
Version:	1.0.6
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d2dfd21a1c2736e9454b7a59152e6c38
URL:		http://pear.php.net/package/Net_Dict/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Cache >= 1.5.2
Requires:	php-pear-Net_Socket >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides a simple API to the DICT Protocol handling all the
network related issues and providing DICT responses in PHP datatypes
to make it easy for a developer to use DICT servers in their programs.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa ta dostarcza proste API do protokołu DICT, dające wszystkie
związane z siecią właściwości oraz dostarczające odpowiedzi DICT w
typach danych PHP, pozwalając na łatwe użycie serwerów DICT w
programach.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
