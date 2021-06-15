import os
import time


os.system('cls')
name = input('\n\nenter the name of your project : ')

try:
  os.system(f'cls && npx create-react-app {name}')
except:
  print(f'Cannot create a project named "{name}" because of npm naming restrictions')
  time.sleep(2)
  # os.execl(sys.executable, sys.executable, *sys.argv)

os.chdir(name)


os.system('cls && del README.md && rmdir src /s /Q && mkdir src && rmdir public /s /Q && mkdir public')
os.chdir('public')


code_for_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>React App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>"""
with open('index.html', 'w') as html:
    html.write(code_for_html)
    html.close()

os.chdir('../src')




code_for_app = """import './App.css';

function App() {
  return (
    <div className="App">
    </div>
  );
}

export default App;"""

code_for_index = """import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.jsx';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);"""




with open('index.js', 'w') as indexjs:
    indexjs.write(code_for_index)
    indexjs.close()

with open('App.jsx', 'w') as App:
    App.write(code_for_app)
    App.close()

with open('App.css', 'w') as css:
    css.write('')
    css.close()



os.chdir('..')
os.system('code .')
os.system('npm start')