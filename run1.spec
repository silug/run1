Name:           run1
Version:        1.12
Release:        3%{?dist}
Summary:        Run a program once at a time
License:        GPL+ or Artistic
URL:            https://github.com/silug/run1
Source0:        https://github.com/silug/run1/archive/master.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  /usr/bin/pod2text
BuildRequires:  /usr/bin/pod2man
Requires:       perl

%description
Run a program once at a time.

%prep
%setup -q -n %{name}-master

%build
pod2text run1 > README
pod2man run1 > run1.1

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 run1 $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0644 run1.1 $RPM_BUILD_ROOT%{_mandir}/man1

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/run1
%{_mandir}/man1/run1.1*

%changelog
* Wed Jul 31 2024 Steven Pritchard <steven.pritchard@gmail.com> 1.12-3
- Rebuild

* Sun Jul 31 2022 Steven Pritchard <steven.pritchard@gmail.com> 1.12-2
- Rebuild

* Tue Jul 18 2017 Steven Pritchard <steve@kspei.com> 1.12-1
- Initial packaging attempt
