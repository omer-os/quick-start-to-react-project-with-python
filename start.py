import os
import colorful as cf

name = input(cf.green('\n\nenter the name of your project : '))

os.system('cls')
os.system(f'npx create-react-app {name}')
os.system(f'cd ./{name}')
os.system('README.md')
os.system('rmdir src /s')
os.system('mkdir src')
os.system('rmdir public /s')
os.system('mkdir public && cd public')


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