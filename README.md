### Purpose

Demo flask app serving via mod_wsgi.

### Notes

- This app assumes a project structure like:

        some_enclosing_directory
            flask_test
                config  # directory
                the_app.py
            env_flasktest


- This app ssumes an entry in our existing apache .conf file like:

        <Directory /path/to/flask_test>
          Order allow,deny
          Allow from all
        </Directory>
        WSGIScriptAlias /path/to/flask_test/config/wsgi.py

---
