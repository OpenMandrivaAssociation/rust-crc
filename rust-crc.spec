# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate crc

Name:           rust-%{crate}
Version:        1.9.0
Release:        2%{?dist}
Summary:        Rust implementation of CRC(16, 32, 64) with support of various standards

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/crc
Source:         %{crates_source}
# Initial patched metadata
# * Update criterion to 0.3, https://github.com/mrhooray/crc-rs/commit/8c2949224a85037c4d8764ea238e7adf840f56f3
Patch0:         crc-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust implementation of CRC(16, 32, 64) with support of various standards.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 11:54:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 22:28:26 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.1-6
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.1-4
- Run tests in infrastructure

* Wed Oct 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.1-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.0-2
- Rebuild for rust-packaging v5

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Wed Nov 22 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Thu Nov 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.5.0-1
- Initial package
