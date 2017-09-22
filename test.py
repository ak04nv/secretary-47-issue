#!/usr/bin/env python
from secretary import Renderer

engine = Renderer()

# Configure custom application filters
with open('text.md') as f:
    md = f.read()
result = engine.render('test.odt', text=md)
output = open('result.odt', 'wb')
output.write(result)
