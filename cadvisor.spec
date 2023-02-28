%define debug_package %{nil}

Name:    cadvisor
Version: 0.37.0
Release: 3
Summary: Analyzes resource usage and performance characteristics of running containers.
License: ASL 2.0
URL:     https://github.com/google/cadvisor

Source0: https://github.com/google/cadvisor/archive/v%{version}.tar.gz
Source1: vendor.tar.gz
Patch0:  use_preinstalled_go-bindata.patch

BuildRequires: golang >= 1.13

Conflicts: cadvisor
Provides:  %{name} = %{version}

%description
cAdvisor (Container Advisor) provides container users an understanding of the resource
usage and performance characteristics of their running containers. 
It is a running daemon that collects, aggregates, processes, and
exports information about running containers. Specifically, for
each container it keeps resource isolation parameters, historical
resource usage, histograms of complete historical resource usage
and network statistics. This data is exported by container and machine-wide.


%prep
%setup -q -T -n %{name}-%{version} -b 0 -b 1
%patch0 -p1

%build
GOFLAGS=-mod=vendor make build

%install
install -D -m 755 cadvisor %{buildroot}%{_bindir}/cadvisor


%files
%defattr(-,root,root,-)
%{_bindir}/cadvisor


%changelog
* Mon Feb 27 2023 misaka00251 <liuxin@iscas.ac.cn> - 0.37.0-3
- Update golang module to latest in order to build on RISC-V

* Fri Jul 22 2022 wo_cow <niuqianqian@huawei.com> - 0.37.0-2
- Fix build err: nothing provides go-bindata

* Tue Dec 15 2020 yangzhao <yangzhao1@kylinos.cn> - 0.37.0-1
- Init project cadvisor
