%define upstream_name    XML-FeedPP
%define upstream_version 0.41

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Parse/write/merge/edit RSS/RDF/Atom syndication feeds
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(XML::TreePP)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'XML::FeedPP' is an all-purpose syndication utility that parses and
publishes RSS 2.0, RSS 1.0 (RDF), Atom 0.3 and 1.0 feeds. It allows you to
add new content, merge feeds, and convert among these various formats. It
is a pure Perl implementation and does not require any other module except
for XML::TreePP.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


