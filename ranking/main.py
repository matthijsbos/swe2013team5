#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from jinja2 import Template

class MainHandler(webapp2.RequestHandler):
    def get(self):
		tmpl = Template(u'''\
		
			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
			<html xmlns="http://www.w3.org/1999/xhtml">
			<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
			<link rel="stylesheet" type="text/css" href="stylesheets/style.css"/>
			<title>Rating</title>
			</head>

			<body>

			<div id="container">
				<div id="quest">
					Question?
				</div>
				
				<a href="#">
				<div id="answleft">
					Answer Left
				</div>
				</a>
				
				<a href="#">
				<div id="answright">
					Answer Right
				</div>
				</a>
			</div>

			</body>
			</html>
		
		''')
		
		self.response.write (tmpl.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
