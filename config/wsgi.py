# -*- coding: utf-8 -*-

""" Prepares application environment.
    Variables assume project setup like:
    some_enclosing_directory
        flasktest
            config  # directory
            the_app.py
        env_flasktest
     """

import os, pprint, sys


## become self-aware, padawan
current_directory = os.path.dirname( os.path.abspath(__file__) )

## vars
ACTIVATE_FILE = os.path.abspath( u'%s/../../env_flasktest/bin/activate_this.py' % current_directory )
PROJECT_DIR = os.path.abspath( u'%s/../../ezb_db_proxy' % current_directory )
PROJECT_ENCLOSING_DIR = os.path.abspath( u'%s/../..' % current_directory )
SITE_PACKAGES_DIR = os.path.abspath( u'%s/../../env_flasktest/lib/python2.6/site-packages' % current_directory )

## virtualenv
execfile( ACTIVATE_FILE, dict(__file__=ACTIVATE_FILE) )  # file loads environmental variables

## sys.path additions
for entry in [PROJECT_DIR, PROJECT_ENCLOSING_DIR, SITE_PACKAGES_DIR]:
 if entry not in sys.path:
   sys.path.append( entry )

from flask_test.the_app import app as application
