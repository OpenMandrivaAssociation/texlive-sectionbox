Name:		texlive-sectionbox
Version:	37749
Release:	2
Summary:	Create fancy boxed ((sub)sub)sections
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sectionbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectionbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sectionbox.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/sectionbox
%doc %{_texmfdistdir}/doc/latex/sectionbox

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
