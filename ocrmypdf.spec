Summary:	An optical character recognition (OCR) text layer to scanned PDF files
Name:		ocrmypdf
Version:	16.10.0
Release:	1
BuildArch:	noarch
Group:		Development/Other
License:	MPL-2.0
URL:		https://github.com/ocrmypdf/OCRmyPDF
Source0:	https://github.com/ocrmypdf/OCRmyPDF/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	tesseract
BuildRequires:	ghostscript
BuildRequires:	unpaper
BuildRequires:	qpdf
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Requires:	tesseract
Requires:	ghostscript
Requires:	pngquant
Requires:	unpaper
Requires:	qpdf

%description
OCRmyPDF adds an optical character recognition (OCR) text layer to scanned
PDF files, allowing them to be searched.

PDF is the best format for storing and exchanging scanned documents.
Unfortunately, PDFs can be difficult to modify. OCRmyPDF makes it easy to
apply image processing and OCR to existing PDFs.

%files
%license LICENSE
%doc README.md
%_bindir/%{name}
%py_puresitedir/%{name}*

#-----------------------------------------------------------------------

%prep
%autosetup -n OCRmyPDF-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py_build

%install
%py_install

