from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World! Python ES 2017'

if __name__ == '__main__':
  app.run()
