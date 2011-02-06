-----------------------
django-socketio-example
-----------------------

This is an example of using Django with Socket.IO, meant to compliment `my blog post on Django with Socket.IO`_.

.. _my blog post on Django with Socket.IO: http://codysoyland.com/2011/feb/6/evented-django-part-one-socketio-and-gevent/

------------
Installation
------------

::

    git clone git://github.com/codysoyland/django-socketio-example.git
    cd django-socketio-example
    easy_install pip
    pip install virtualenv
    virtualenv .
    source ./bin/activate
    pip install -r pip_requirements.txt

-------
Running
-------

Start the example server::

    ./run_example.py

Then point your browser to http://localhost:9000/.
