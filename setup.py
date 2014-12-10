from distutils.core import setup
import py2exe
setup(
        windows=['main_ui.py','pyperclip.py','main.py'],
        options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "dll_excludes": ["MSVCP90.dll"]
                }
        }
)