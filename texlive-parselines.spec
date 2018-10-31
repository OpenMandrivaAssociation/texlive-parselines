# revision 21475
# category Package
# catalog-ctan /macros/latex/contrib/parselines
# catalog-date 2011-02-19 16:41:47 +0100
# catalog-license lppl1.3
# catalog-version 1.4
Name:		texlive-parselines
Version:	1.4
Release:	11
Summary:	Apply a macro to each line of an environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parselines
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines an environment "parse lines" which
processes each line of an environment with a macro. An example
of shading the lines of an environment is given.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/parselines/parselines.sty
%doc %{_texmfdistdir}/doc/latex/parselines/README
%doc %{_texmfdistdir}/doc/latex/parselines/parselines.pdf
#- source
%doc %{_texmfdistdir}/source/latex/parselines/parselines.drv
%doc %{_texmfdistdir}/source/latex/parselines/parselines.dtx
%doc %{_texmfdistdir}/source/latex/parselines/parselines.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 754647
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 719199
- texlive-parselines
- texlive-parselines
- texlive-parselines
- texlive-parselines

