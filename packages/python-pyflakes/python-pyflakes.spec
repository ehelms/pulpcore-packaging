# Created by pyp2rpm-3.3.3
%global pypi_name pyflakes

Name:           python-%{pypi_name}
Version:        2.3.1
Release:        1%{?dist}
Summary:        passive checker of Python programs

License:        MIT
URL:            https://github.com/PyCQA/pyflakes
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/pyflakes
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 31 2021 Evgeni Golov 2.3.1-1
- Update to 2.3.1

* Fri Mar 19 2021 Evgeni Golov 2.3.0-1
- Update to 2.3.0

* Tue Jun 23 2020 Evgeni Golov - 2.2.0-1
- Initial package.
