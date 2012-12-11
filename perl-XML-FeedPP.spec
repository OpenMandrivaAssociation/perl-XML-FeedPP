%define upstream_name    XML-FeedPP
%define upstream_version 0.43

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Parse/write/merge/edit RSS/RDF/Atom syndication feeds
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(XML::TreePP)
BuildArch:	noarch

%description
'XML::FeedPP' is an all-purpose syndication utility that parses and
publishes RSS 2.0, RSS 1.0 (RDF), Atom 0.3 and 1.0 feeds. It allows you to
add new content, merge feeds, and convert among these various formats. It
is a pure Perl implementation and does not require any other module except
for XML::TreePP.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 672884
- update to new version 0.43

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.420.0-2
+ Revision: 657861
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2011.0
+ Revision: 596705
- update to 0.42

* Mon Jul 26 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.410.0-3mdv2011.0
+ Revision: 560579
- perl rebuild

* Fri Mar 12 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.410.0-2mdv2011.0
+ Revision: 518568
- Bump release

* Sun Feb 28 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.410.0-1mdv2010.1
+ Revision: 512541
- Import
- import perl-XML-FeedPP


* Sat Feb 27 2010 cpan2dist 0.41-1mdv
- initial mdv release, generated with cpan2dist
