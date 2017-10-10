%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-service-types
%global module_name os_service_types

%if 0%{?fedora}
%global with_python3 1
%endif

%global common_desc \
OsServiceTypes is a Python library for consuming OpenStack sevice-types-authority data \
The OpenStack Service Types Authority contains information about official \
OpenStack services and their historical service-type aliases. \
The data is in JSON and the latest data should always be used. This simple \
library exists to allow for easy consumption of the data, along with a built-in \
version of the data to use in case network access is for some reason not possible \
and local caching of the fetched data.

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Python library for consuming OpenStack sevice-types-authority data

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git

%description
%{common_desc}

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python-subunit
BuildRequires:  python2-oslotest
BuildRequires:  python-testscenarios
BuildRequires:  python-requests-mock
BuildRequires:  python2-keystoneauth1
BuildRequires:  python2-setuptools

Requires:       python2-pbr >= 2.0.0
%description -n python2-%{pypi_name}
%{common_desc}

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-subunit
BuildRequires:  python3-oslotest
BuildRequires:  python3-testscenarios
BuildRequires:  python3-requests-mock
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-setuptools

Requires:       python3-pbr >= 2.0.0
%description -n python3-%{pypi_name}
%{common_desc}
%endif

%package -n python-%{pypi_name}-doc
Summary:        %{pypi_name} documentation

BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-sphinx

%description -n python-%{pypi_name}-doc
%{common_desc}


Documentation for %{pypi_name}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?with_python3}
%py3_build
%endif
%py2_build
# generate html docs
%{__python2} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
%endif

%py2_install


%check
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%{__python2} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python2_sitelib}/%{module_name}
%{python2_sitelib}/%{module_name}-%{upstream_version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/%{module_name}-%{upstream_version}-py?.?.egg-info
%endif

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html

%changelog