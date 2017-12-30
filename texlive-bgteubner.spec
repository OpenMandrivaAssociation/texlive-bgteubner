Name:		texlive-bgteubner
Version:	2.11
Release:	1
Summary:	Class for producing books for the publisher "Teubner Verlag"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bgteubner
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bgteubner.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bgteubner.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bgteubner.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bgteubner document class has been programmed by order of
the Teubner Verlag, Wiesbaden, Germany, to ensure that books of
this publisher have a unique layout. Unfortunately, most of the
documentation is only available in German. Since the document
class is intended to generate a unique layout, many things
(layout etc.) are fixed and cannot be altered by the user. If
you want to use the document class for another purpose than
publishing with the Teubner Verlag, this may arrise unwanted
restrictions (For instance, the document class provides only
two paper sizes: DIN A-5 and 17cm x 24cm; only two font
families are supported: Times and European Computer Modern).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/bgteubner
%{_texmfdistdir}/makeindex/bgteubner
%{_texmfdistdir}/tex/latex/bgteubner
%doc %{_texmfdistdir}/doc/latex/bgteubner
#- source
%doc %{_texmfdistdir}/source/latex/bgteubner

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}
