#! /usr/bin/env python
from app import app
import os
from flask import render_template,Flask

app.run(debug=True,host="0.0.0.0",port=8080)
