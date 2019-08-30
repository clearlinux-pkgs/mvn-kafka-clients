#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-kafka-clients
Version  : 2.0.0
Release  : 4
URL      : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.jar
Source0  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.jar
Source1  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.10.2.1/kafka-clients-0.10.2.1.jar
Source2  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.10.2.1/kafka-clients-0.10.2.1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.11.0.2/kafka-clients-0.11.0.2.jar
Source4  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.11.0.2/kafka-clients-0.11.0.2.pom
Source5  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.jar
Source6  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.pom
Source7  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.2/kafka-clients-0.8.2.2.jar
Source8  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.2/kafka-clients-0.8.2.2.pom
Source9  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.9.0.1/kafka-clients-0.9.0.1.jar
Source10  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.9.0.1/kafka-clients-0.9.0.1.pom
Source11  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.pom
Source12  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.0.1/kafka-clients-2.0.1.jar
Source13  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.0.1/kafka-clients-2.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-kafka-clients-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-kafka-clients package.
Group: Data

%description data
data components for the mvn-kafka-clients package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.10.2.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.10.2.1/kafka-clients-0.10.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.10.2.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.10.2.1/kafka-clients-0.10.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.11.0.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.11.0.2/kafka-clients-0.11.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.11.0.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.11.0.2/kafka-clients-0.11.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.2/kafka-clients-0.8.2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.2
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.2/kafka-clients-0.8.2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.9.0.1
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.9.0.1/kafka-clients-0.9.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.9.0.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.9.0.1/kafka-clients-0.9.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.1/kafka-clients-2.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.1
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.1/kafka-clients-2.0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.10.2.1/kafka-clients-0.10.2.1.jar
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.10.2.1/kafka-clients-0.10.2.1.pom
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.11.0.2/kafka-clients-0.11.0.2.jar
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.11.0.2/kafka-clients-0.11.0.2.pom
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.jar
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.pom
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.2/kafka-clients-0.8.2.2.jar
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.8.2.2/kafka-clients-0.8.2.2.pom
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.9.0.1/kafka-clients-0.9.0.1.jar
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/0.9.0.1/kafka-clients-0.9.0.1.pom
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.jar
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.pom
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.1/kafka-clients-2.0.1.jar
/usr/share/java/.m2/repository/org/apache/kafka/kafka-clients/2.0.1/kafka-clients-2.0.1.pom
