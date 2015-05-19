%define name euca-deploy
%define version 0.1
%define unmangled_version 0.1
%define unmangled_version 0.1
%define release 1

Summary: Tool for installing Eucalyptus
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{tarball_basedir}.tar.xz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Vic Iglesias <viglesiasce@gmail.com>
Url: https://github.com/viglesiasce/euca-deploy/

Requires: fabric PyYaml

%description
# Euca Deploy

This is a harness for running the Eucalyptus cookbook against a distributed system of nodes without a dependency on a Chef Server. We are using fabric and chef-zero to emulate the functionality of a chef-server. 

## Install

### On a CentOS 6 system:

    yum install -y python-devel gcc git python-setuptools
    easy_install fabric PyYAML
    curl -L https://www.opscode.com/chef/install.sh | sudo bash -s -- -P chefdk
    git clone https://github.com/viglesiasce/euca-deploy
    cd euca-deploy
    python setup.py install
    
## Lifecycle Actions
The cloud lifecycle is broken down into many phases:

### Configure
The configuration is written in YAML and uses the Chef environment structure. Examples can be found in the examples directory. For a full list of attributes that can be set look at the [Eucalyptus Cookbook attributes](https://github.com/eucalyptus/eucalyptus-cookbook/blob/testing/attributes/default.rb). Edit the etc/environment.yml file to match your deployment topology and configuration.

### Validate
#### Not yet implemented!!!
In this stage we run validations against the configuration file to ensure that the deployment will succeed as we expect.

### Prepare
This step ensures that Chef is installed on all servers and that we can SSH to all of them. It is nice to know that we are on good footing before we get going with the deployment.

    euca-deploy prepare -p <root-ssh-password-for-deployment-systems>

### Bootstrap
This step deploys the CLC and initializes the database. Here we are getting a bit deeper and if complete, we can assume that we've are on good footing to continue deploying the rest of the cloud.

    euca-deploy bootstrap -p <root-ssh-password-for-deployment-systems>
  
### Provision
Provisions the rest of the system or update the configuration of an existing system. If you change anything in your environment.yml, you can use this to push that change out to your cloud.

    euca-deploy provision -p <root-ssh-password-for-deployment-systems>
    
### Debug
#### Not yet implemented!!!
This step will grab all necessary information from a system in order to provide artifacts for use in debugging a problem.
    
    
    


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
