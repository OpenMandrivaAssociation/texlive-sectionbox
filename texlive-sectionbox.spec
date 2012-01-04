# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sectionbox
# catalog-date 2007-02-26 21:24:31 +0100
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-sectionbox
Version:	1.01
Release:	2
Summary:	Create fancy boxed ((sub)sub)sections
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sectionbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectionbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectionbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Sectionbox is a LaTeX package for putting fancy colored boxes
around sections, subsections, and subsubsections, especially
for use in posters, etc. It was designed with the sciposter
class in mind, and certainly works with that class and with
derived classes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sectionbox/sectionbox.sty
%doc %{_texmfdistdir}/doc/latex/sectionbox/README
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/000074Bpatspec.png
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/000074Bzones.jpg
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/000175Bpatspec.png
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/000175Bzones.jpg
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/002000AApatspec.png
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/002000AAzones.jpg
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/lambda2.jpg
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/lenna10connect.jpg
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/lenna10pct.jpg
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/lenna10smooth.jpg
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/orig.jpg
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/sectionboxexample.bib
%doc %{_texmfdistdir}/doc/latex/sectionbox/example/sectionboxexample.tex
%doc %{_texmfdistdir}/doc/latex/sectionbox/sectionboxmanual.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
