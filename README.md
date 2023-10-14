# Overview

In this project, I tried to make a folder on a server accessible through a web API to users with various permission levels.

This program utilizes a Flask server as a web-based API to handle viewing and uploading to a database. On a network start server.py, then navigate to the IP address and port of the server and log in.

I chose this project because I wanted to come up an AirDrop alternative, where I could share files to friends in an easy way while implementing some type of security.

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

The architecture of this program is client-server.

It uses TCP communication protocol on port 5000.

The messages sent between the client and server are of HTTP protocol.

# Development Environment

This software was built in a Python Miniconda environment in VSCode.

Additional languages used were HTML and CSS. 
Python libraries used were flask, flask_login, flask_uploads, logging, secret, os, and werkzeug.utils.

# Useful Websites

* [Flask Quickstart](https://flask.palletsprojects.com/en/2.3.x/quickstart/))
* [Flask Login Manager](https://flask-login.readthedocs.io/en/latest/)
* [Flask Upload Manager](https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/)

# Future Work

Features in need of further development:
* Page navigation
* Fix download button
* Beautify with better CSS
