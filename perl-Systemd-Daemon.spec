#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Systemd-Daemon
Version  : 0.07
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/V/VD/VDB/Systemd-Daemon-0.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/V/VD/VDB/Systemd-Daemon-0.07.tar.gz
Summary  : 'Write systemd-aware daemons in Perl'
Group    : Development/Tools
License  : GPL-3.0
Requires: perl-Systemd-Daemon-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::CheckLib)
BuildRequires : perl(Devel::Symdump)
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(File::Which)
BuildRequires : perl(IPC::Run3)
BuildRequires : perl(IPC::System::Simple)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Readonly)
BuildRequires : perl(Test::DiagINC)
BuildRequires : perl(Try::Tiny)
BuildRequires : pkgconfig(libsystemd)

%description
WHAT?
perl-Systemd-Daemon is Perl interface (aka "binding") to the part of libsystemd
declared in <systemd/sd-daemon.h>. perl-Systemd-Daemon allows developers to
write systemd-aware daemons in Perl.

%package dev
Summary: dev components for the perl-Systemd-Daemon package.
Group: Development
Provides: perl-Systemd-Daemon-devel = %{version}-%{release}
Requires: perl-Systemd-Daemon = %{version}-%{release}

%description dev
dev components for the perl-Systemd-Daemon package.


%package perl
Summary: perl components for the perl-Systemd-Daemon package.
Group: Default
Requires: perl-Systemd-Daemon = %{version}-%{release}

%description perl
perl components for the perl-Systemd-Daemon package.


%prep
%setup -q -n Systemd-Daemon-0.07
cd %{_builddir}/Systemd-Daemon-0.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Systemd::Daemon.3
/usr/share/man/man3/Systemd::Daemon::Stub.3
/usr/share/man/man3/Systemd::Daemon::XS.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/Systemd/Daemon.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/Systemd/Daemon/Stub.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/Systemd/Daemon/XS.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/Systemd/Daemon/XS/Inline.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/auto/Systemd/Daemon/XS/Inline/Inline.so
