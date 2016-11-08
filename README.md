Prerequisite
============
install the following:
```
sudo apt-get install python-dev
```
Python IDE:
https://www.jetbrains.com/pycharm/
add pycharm.sh to user bin path:
```
cd /usr/bin
sudo ln -s /path/to/pycharm/bin/pycharm.sh pycharm
```

GIT (if you don't have one yet) :
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Google Cloud SDK:
https://cloud.google.com/sdk/


How To
=======
## Install required packages
```
pip install -r requirements.txt -t packages
```

## run on localhost
```
dev_appserver.py .
```

Resources
=========

https://cloud.google.com/appengine/docs/python/quickstart

http://turbogears.readthedocs.io/en/latest/turbogears/minimal/index.html

http://turbogears.readthedocs.io/en/latest/cookbook/deploy/appengine/

https://googlecloudplatform.github.io/google-cloud-python/
