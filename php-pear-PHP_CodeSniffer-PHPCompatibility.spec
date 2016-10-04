%define		ruleset	PHPCompatibility
Summary:	PHP Compatibility Coding Standard for PHP_CodeSniffer
Name:		php-pear-PHP_CodeSniffer-%{ruleset}
Version:	7.0.6
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	https://github.com/wimg/PHPCompatibility/archive/%{version}/%{ruleset}-%{version}.tar.gz
# Source0-md5:	77b3b20bde46a3d6c0563ebd7776cfdc
URL:		http://techblog.wimgodden.be/tag/codesniffer/
Requires:	php-pear
Requires:	php-pear-PHP_CodeSniffer >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ruledir	  %{php_pear_dir}/PHP/CodeSniffer/Standards/%{ruleset}

%description
This is a set of sniffs for PHP_CodeSniffer that checks for PHP
version compatibility.

%prep
%setup -q -n %{ruleset}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruledir}
cp -a Sniffs ruleset.xml $RPM_BUILD_ROOT%{ruledir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{ruledir}
