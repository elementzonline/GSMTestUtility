# setup.py
from distutils.core import setup
import py2exe
 
setup(
	windows=[{"script":"mainGUI.py"}], 
	options={
		"py2exe":{
		"includes":["sip"],
		"dll_excludes": ["MSVCP90.dll"]
		}
	}
)
