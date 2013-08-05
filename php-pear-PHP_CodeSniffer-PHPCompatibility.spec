%define		ruleset	PHPCompatibility
Summary:	PHP Compatibility Coding Standard for PHP_CodeSniffer
Name:		php-pear-PHP_CodeSniffer-%{ruleset}
Version:	1.1.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	https://github.com/wimg/PHPCompatibility/tarball/master/%{ruleset}-%{version}.tar.gz
# Source0-md5:	03e220a1fa185a36faf3631478a15dbd
URL:		http://techblog.wimgodden.be/tag/codesniffer/
Requires:	php-pear
Requires:	php-pear-PHP_CodeSniffer >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ruledir	  %{php_pear_dir}/PHP/CodeSniffer/Standards/%{ruleset}

%description
This is a set of sniffs for PHP_CodeSniffer that checks for PHP
version compatibility.

%prep
%setup -qc
mv *-%{ruleset}-*/* .

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
