%{?scl:%scl_package nodejs-spdx}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-spdx

%global npm_name spdx
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-spdx
Version:	0.4.1
Release:	2%{?dist}
Summary:	SPDX License Expression Syntax parser
Url:		https://github.com/kemitchell/spdx.js
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	Apache-2.0

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel


%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(docco)
BuildRequires:	%{?scl_prefix}npm(fixpack)
BuildRequires:	%{?scl_prefix}npm(jison)
BuildRequires:	%{?scl_prefix}npm(jscs)
BuildRequires:	%{?scl_prefix}npm(jshint)
BuildRequires:	%{?scl_prefix}npm(jsmd)
%endif

BuildRequires:	%{?scl_prefix}npm(spdx-license-ids)

Requires:	%{?scl_prefix}npm(spdx-license-ids)

%description
SPDX License Expression Syntax parser

%prep
%setup -q -n package

rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json source/*.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/spdx

%doc README.md
%doc LICENSE.md

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.4.1-2
- rebuilt

* Mon Nov 23 2015 Tomas Hrcka <thrcka@redhat.com> - 0.4.1-1
- Initial build
