try:
  import requests, os, shutil , time , subprocess, glob
  from bs4 import BeautifulSoup
except:
  import os
  os.system('pip install flask')
  os.system('pip install bs4')

print('''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▄▄▄▒▒▒█▒▒▒▒▄▒▒▒▒▒▒▒▒
▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒
░█▀█▀█░█▀██░█▀█░█▄█▄█░
░█▀█▀█░█▀████▀█░█▄█▄█░
████████▀█████████████
''')
# City art ascii for console.

# Creating the flask app server.
def addroutes():

    files = glob.glob(f"website/*")
    # Getting all the files in web for the naming and creating of diffrent routes/website direcions.

    init = f"""try:
  import requests, os, shutil , time , subprocess, glob
  from bs4 import BeautifulSoup
  import flask 
  from flask import Flask, render_template , redirect , request
  
except:
  import os
  os.system('pip install flask')
  os.system('pip install bs4')

  import requests, os, shutil , time , subprocess, glob
  from bs4 import BeautifulSoup
  import flask 
  from flask import Flask, render_template , redirect , request

template_dir = os.path.abspath('website')
static_dir = os.path.abspath('website/assets')

app = Flask(__name__, template_folder=template_dir , static_folder=static_dir)

app.config['TEMPLATES_AUTO_RELOAD'] = True
  
template_dir = os.path.abspath('website')
static_dir = os.path.abspath('website/assets')

app = Flask(__name__, template_folder=template_dir , static_folder=static_dir)

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')

    """ 

    open('app.py', 'w+').write(init)
    # Config and first index route for app server, using w+ to recreate the file for updates / future appends


    # Simple for loop to get all the html files in the web dir and removing all the extra stuff like .html and / from files. 
    for html in files:
        if "index" in html:
            pass
        else:
            if html.endswith('html'):
                html = html.strip('website').strip('.html').strip('/')
                cleanedr = f"""\n #==== New Route ====#
@app.route('/{html}')
def {html}():
    return render_template('{html}.html')

    """
                open('app.py', 'a+').write(cleanedr)
            else:
                pass
        # Creating the route and adding it to  app.py file. using a+ to append the file with cleaned code.
        pass


    print('[*] Added all routes...')

    last = f"""\nif '__main__' == __name__:
    app.run(host='0.0.0.0', port='5000', debug=True)
    """ 

    open('app.py', 'a+').write(last)
    # Creating the final part to run on all host (creating a live server from repl).

addroutes()
# Calling the addroutes before starting the app.py.

subprocess.Popen(('python3', 'app.py')) 

while True:
  addroutes()
  time.sleep(1)
