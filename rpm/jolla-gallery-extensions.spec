# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       jolla-gallery-extensions

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Extension for jolla-gallery
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    TODO
URL:        https://github.com/SfietKonstantin/jolla-gallery-extensions
Source0:    %{name}-%{version}.tar.bz2
Source100:  jolla-gallery-extensions.yaml
Requires:   patch
Requires:   sailfish-components-gallery-qt5 = 0.0.41
Requires:   jolla-gallery = 0.1.45
BuildRequires:  pkgconfig(Qt5Core)

%description
Extension for jolla-gallery.
Brings a slightly better user 
experience for videos.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%preun
# >> preun
/opt/SfietKonstantin/extensions/jolla-gallery/preun.sh
# << preun

%post
# >> post
/opt/SfietKonstantin/extensions/jolla-gallery/post.sh
# << post

%files
%defattr(-,root,root,-)
/opt/SfietKonstantin/extensions/jolla-gallery
# >> files
# << files