# -*- mode: python -*-
#from here run: python #C:\Users\Felix\Downloads\Programming\pyinstaller-1.5\Build.py main.spec
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\unpackTK.py'), os.path.join(HOMEPATH,'support\\useTK.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'C:\\Users\\Felix\\Documents\\Projects Temp\\lord-of-ultima-tools\\src\\main.py', os.path.join(HOMEPATH,'support\\removeTK.py')],
             pathex=['C:\\Users\\Felix\\Documents\\Projects Temp\\lord-of-ultima-tools'])
pyz = PYZ(a.pure)
exe = EXE(TkPKG(), pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('C:\\Users\\Felix\\Documents\\Projects Temp\\lord-of-ultima-tools\\dist', 'LoU_tools.exe'),
          debug=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\Felix\\Documents\\Projects Temp\\lord-of-ultima-tools\\src\\images\\logo256.ico')
app = BUNDLE(exe,
             name=os.path.join('C:\\Users\\Felix\\Documents\\Projects Temp\\lord-of-ultima-tools\\dist', 'LoU_tools.exe.app'))
