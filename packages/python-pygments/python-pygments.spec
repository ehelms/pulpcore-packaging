# Created by pyp2rpm-3.3.3
%global pypi_name Pygments
%global srcname pygments

Name:           python-%{srcname}
Version:        2.8.1
Release:        1%{?dist}
Summary:        Pygments is a syntax highlighting package written in Python

License:        BSD License
URL:            https://pygments.org/
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

BuildArch:      noarch

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/pygmentize
%{python3_sitelib}/pygments
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Mar 19 2021 Evgeni Golov 2.8.1-1
- Update to 2.8.1

* Thu Oct 29 2020 Evgeni Golov 2.7.2-1
- Update to 2.7.2

* Tue Aug 25 2020 Evgeni Golov - 2.6.1-1
- Initial package.
