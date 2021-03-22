Review
* functions
* defined with def keyword
* def [function_name](optional_param1, optional_param2=1):
* return [your_object]
* passing parameters in a positional matter, order counts
* passing by keyword, order does not matter
  * dev = a_function(b=1, c=2, a=3)
* return values
* hide complexity
* sharing and reuse

Quokka example
* ui, db, quokka, quokka-ui
* flask
* flask run --host=0.0.0.0
* npm start

Flask applications
* quickstart
* https://flask.palletsprojects.com/en/1.1.x/quickstart/
  ```
  from flask import Flask
  app = Flask(__name__)

  @app.route('/')
  def hello_world():
      return 'Hello, World!'  
  ```
* larger applications
* https://flask.palletsprojects.com/en/1.1.x/patterns/packages/
* \_\_init\_\_.py