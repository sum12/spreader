# -*- mode: python -*-
a = Analysis(['main.py', 'main_ui.py', 'pyperclip.py'],
             pathex=['C:\\Users\\sumit\\workspace\\spreader\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
