Name:		texlive-parselines
Version:	21475
Release:	1
Summary:	Apply a macro to each line of an environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parselines
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parselines.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
