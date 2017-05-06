Name:           ocrmypdf
Version:        4.5.6
Release:        1
Summary:        Next-generation distributed version control
BuildArch:	noarch
Group:          Development/Other
License:        GPLv2+
URL:            http://www.bazaar-vcs.org/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	tesseract
BuildRequires:	ghostscript
BuildRequires:	unpaper
BuildRequires:	qpdf
Requires:	tesseract
Requires:	ghostscript
Requires:	unpaper
Requires:	qpdf

%description
Bazaar is a distributed revision control system. It allows team members to
branch and merge upstream code very easily.

Distributed revision control systems allow multiple people to have their
own branch of a project, and merge code efficiently between them. This
enables new contributors to immediately have access to the full tools that
previously have been limited to just the committers to a project.

%prep
%setup -q -n %{name}-%{version}

%build
export LDFLAGS=-ldl
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc  README.rst LICENSE.rst
%_bindir/%{name}
%py_puresitedir/%{name}*
