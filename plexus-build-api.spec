Name:           plexus-build-api
Version:        0.0.7
Release:        11%{?dist}
Summary:        Plexus Build API

License:        ASL 2.0
URL:            https://github.com/sonatype/sisu-build-api
#Fetched from https://github.com/sonatype/sisu-build-api/tarball/plexus-build-api-0.0.7
Source0:        sonatype-sisu-build-api-plexus-build-api-0.0.7-0-g883ea67.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{name}-migration-to-component-metadata.patch

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-utils
BuildRequires: forge-parent
BuildRequires: spice-parent
BuildRequires: junit
BuildRequires: plexus-containers-component-metadata
BuildRequires: maven-shared-reporting-impl
BuildRequires: plexus-digest

%description
Plexus Build API

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n sonatype-sisu-build-api-f1f8849
cp -p %{SOURCE1} .

%patch0 -p1

%mvn_file : plexus/%{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.0.7-11
- Mass rebuild 2013-12-27

* Thu Aug 15 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.7-10
- Migrate away from mvn-rpmbuild (#997433)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.7-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.0.7-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - error: source 0 defined multiple times
- Install license files
- Resolves: rhbz#880200

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 0.0.7-5
- Migration to plexus-containers-container-default

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 04 2011 Jaromir Capik <jcapik@redhat.com> - 0.0.7-2
- Migration from plexus-maven-plugin to plexus-containers-component-metadata

* Tue Aug 2 2011 Alexander Kurtakov <akurtako@redhat.com> 0.0.7-1
- Update to latest upstream version.

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.6-7
- Add spice-parent to Requires

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 0.0.6-6
- Build with maven.
- Fix requires.
- Guidelines fixes.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 26 2010 Hui Wang <huwnag@redhat.com> 0.0.6-3
- Add missing requires

* Wed May 26 2010 Hui Wang <huwnag@redhat.com> 0.0.6-2
- Change JPP-%{name}.pom to JPP.plexus-%{name}.pom

* Wed May 19 2010 Hui Wang <huwang@redhat.com> 0.0.6-1
- Initial version of the package
