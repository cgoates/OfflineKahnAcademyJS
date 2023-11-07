import subprocess, webbrowser, sys, os
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Find the directory of this script, or the executable if packaged by PyInstaller --onefile
# Note that this code snippet won't work with PyInstaller without the --onefile flag.
# See https://stackoverflow.com/questions/404744 for more information if you are interested
# in changing that.
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

# Start an http server on localhost
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)

# Open VSCode to the javascript file that includes the custom processingJS code.
subprocess.Popen(['Code', f'{application_path}\\mycode.js'], shell=True)

# Open a web browser to the location of the served files.
webbrowser.open('http://localhost:8000')

# Continuously serve the files until this script is killed.
httpd.serve_forever()