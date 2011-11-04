# revision 21475
# category Package
# catalog-ctan /macros/latex/contrib/parselines
# catalog-date 2011-02-19 16:41:47 +0100
# catalog-license lppl1.3
# catalog-version 1.4
Name:		texlive-parselines
Version:	1.4
Release:	1
Summary:	Apply a macro to each line of an environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parselines
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package defines an environment "parse lines" which
processes each line of an environment with a macro. An example
of shading the lines of an environment is given.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
