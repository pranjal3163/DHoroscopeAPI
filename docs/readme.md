As suggested by https://github.com/PyMySQL/mysqlclient-python
You need to install 2 packages on you amazon linux ec2 instance:
sudo yum install python-devel mysql-devel

Name of the packages are more specific in amazon linux.
yum list | grep python3
shows you a list of python-devel packages
Install the package that meets your requirement.

sudo yum list | grep mysql
shows you a list of mysql-devel packages
Install the package that meets your requirement

In my case
sudo yum install python36-devel
yum install mysql57-devel
did the job.