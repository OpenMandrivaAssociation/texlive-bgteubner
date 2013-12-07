# revision 25892
# category Package
# catalog-ctan /macros/latex/contrib/bgteubner
# catalog-date 2012-04-08 14:50:51 +0200
# catalog-license lppl
# catalog-version 2.02
Name:		texlive-bgteubner
Version:	2.02
Release:	5
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
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteuabbr.bst
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteuabbr2.bst
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteupln.bst
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteupln2.bst
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteupln3.bst
%{_texmfdistdir}/makeindex/bgteubner/bgteubner.ist
%{_texmfdistdir}/makeindex/bgteubner/bgteuglo.ist
%{_texmfdistdir}/makeindex/bgteubner/bgteuglochar.ist
%{_texmfdistdir}/tex/latex/bgteubner/bgteubner.cls
%{_texmfdistdir}/tex/latex/bgteubner/hhfixme.sty
%{_texmfdistdir}/tex/latex/bgteubner/hhsubfigure.sty
%{_texmfdistdir}/tex/latex/bgteubner/ptmxcomp.sty
%doc %{_texmfdistdir}/doc/latex/bgteubner/01b.png
%doc %{_texmfdistdir}/doc/latex/bgteubner/02b.png
%doc %{_texmfdistdir}/doc/latex/bgteubner/ChangeLog
%doc %{_texmfdistdir}/doc/latex/bgteubner/LIESMICH
%doc %{_texmfdistdir}/doc/latex/bgteubner/Makefile.hhsubfigure
%doc %{_texmfdistdir}/doc/latex/bgteubner/Makefile.source
%doc %{_texmfdistdir}/doc/latex/bgteubner/Makefile.src
%doc %{_texmfdistdir}/doc/latex/bgteubner/README
%doc %{_texmfdistdir}/doc/latex/bgteubner/README.hhsubfigure
%doc %{_texmfdistdir}/doc/latex/bgteubner/ToDo
%doc %{_texmfdistdir}/doc/latex/bgteubner/anhang.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/befehlsreferenz.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/beispiel1.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteubner-17x24-cm.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteubner-17x24-mathtime.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteubner-17x24-times.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteubner-a5-cm.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteubner-a5-times.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteubner-with-hyperref.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteubner.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteubner.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteucls.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bgteuversion.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild4c.png
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_ganz.eps
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_ganz.fig
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_ganz.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_mitte.eps
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_mitte.fig
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_mitte.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_oben.eps
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_oben.fig
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_oben.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_oben_unten.eps
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_oben_unten.fig
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_oben_unten.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_umflossen.eps
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_umflossen.fig
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_umflossen.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_unten.eps
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_unten.fig
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_unten.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang.eps
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang.fig
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang2.eps
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang2.fig
%doc %{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang2.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/bilder.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/cdcover.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/checkliste.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/einleitung.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/formelzeichen.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/getversion.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/globales.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/hyphenation.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/index.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/installation.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/kapitel2.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/literatur.bib
%doc %{_texmfdistdir}/doc/latex/bgteubner/literatur.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/ltxdoc.cfg
%doc %{_texmfdistdir}/doc/latex/bgteubner/manifest.txt
%doc %{_texmfdistdir}/doc/latex/bgteubner/math-cm.info
%doc %{_texmfdistdir}/doc/latex/bgteubner/math-cm.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/math-cm.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/math-mathtime.info
%doc %{_texmfdistdir}/doc/latex/bgteubner/math-mathtime.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/math-mathtime.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/math.info
%doc %{_texmfdistdir}/doc/latex/bgteubner/math.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/math.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/optionen-advanced.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/testquick.exercise
%doc %{_texmfdistdir}/doc/latex/bgteubner/testquick.info
%doc %{_texmfdistdir}/doc/latex/bgteubner/testquick.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/testtimes.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/tex_aufruf.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/tex_bilder.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/tex_globales.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/tex_textelemente.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/tex_typographie.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/tex_verzeichnisse.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/textelemente.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/times-ja2.png
%doc %{_texmfdistdir}/doc/latex/bgteubner/times-nein2.png
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch1.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch1.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch1a.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch1a.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch2.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch2.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch2a.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch2a.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch3.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch3.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch3a.pdf
%doc %{_texmfdistdir}/doc/latex/bgteubner/umbruch3a.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/usefiles.txt
%doc %{_texmfdistdir}/doc/latex/bgteubner/verzeichnisse.tex
%doc %{_texmfdistdir}/doc/latex/bgteubner/vorwort.tex
#- source
%doc %{_texmfdistdir}/source/latex/bgteubner/bgteucls.dtx
%doc %{_texmfdistdir}/source/latex/bgteubner/bgteucls.ins
%doc %{_texmfdistdir}/source/latex/bgteubner/hhsubfigure.dtx
%doc %{_texmfdistdir}/source/latex/bgteubner/hhsubfigure.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.02-1
+ Revision: 790532
- Import texlive-bgteubner
- Import texlive-bgteubner

