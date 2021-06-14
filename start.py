import os
import colorful as cf

name = input(cf.green('\n\nenter the name of your project : '))

os.system(f'cls && npx create-react-app {name}')

os.system(f'cd ./{name}')
os.system('README.md')
os.system('rmdir src /s')
os.system('mkdir src')
os.system('rmdir public /s')
os.system('mkdir public && cd public')

code_for_html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>React App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
"""


code_for_app = """
import './App.css';

function App() {
  return (
    <div className="App">
    </div>
  );
}

export default App;
"""

code_for_index = """
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.jsx';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
"""

with open('index.html') as html:
    html.write(code_for_html)
    html.close()


os.system('cd..')

os.system('cd src')
with open('index.js') as index:
    index.write(code_for_index)
    index.close()
with open('App.jsx') as App:
    App.write(code_for_app)
    App.close()


os.system('code .')