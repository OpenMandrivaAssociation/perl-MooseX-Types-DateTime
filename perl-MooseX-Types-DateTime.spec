%define upstream_name    MooseX-Types-DateTime
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	L<DateTime> related constraints and coercions for
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Locale)
BuildRequires:	perl(DateTime::TimeZone)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This module packages several the Moose::Util::TypeConstraints manpage with
coercions, designed to work with the the DateTime manpage suite of objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 654261
- rebuild for updated spec-helper

* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 488019
- import perl-MooseX-Types-DateTime


* Sat Jan 09 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
