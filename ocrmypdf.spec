Summary:	An optical character recognition (OCR) text layer to scanned PDF files
Name:		ocrmypdf
Version:	16.7.0
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
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling) = 1.25
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Requires:	tesseract
Requires:	ghostscript
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
export LDFLAGS=-ldl
%py_build

%install
%py_install

