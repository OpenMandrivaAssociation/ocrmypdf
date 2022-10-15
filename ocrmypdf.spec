%define oname OCRmyPDF
%define name %(echo %oname | tr [:upper:] {:lower:])

Summary:	An optical character recognition (OCR) text layer to scanned PDF files
Name:		ocrmypdf
Version:	14.0.1
Release:	1
BuildArch:	noarch
Group:		Development/Other
License:	MPL-2.0
URL:		https://github.com/ocrmypdf/%{oname}
Source0:	https://github.com/ocrmypdf/%{oname}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	tesseract
BuildRequires:	ghostscript
BuildRequires:	unpaper
BuildRequires:	qpdf
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

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
%doc  README.rst LICENSE.rst
%_bindir/%{name}
%py_puresitedir/%{name}*

#-----------------------------------------------------------------------

%prep
%autosetup -n %{oname}-%{version}

%build
export LDFLAGS=-ldl
%py_build

%install
%py_install

