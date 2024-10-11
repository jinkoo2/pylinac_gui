# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pylinac_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('./_venv2/Lib/site-packages/babel/locale-data', 'babel/locale-data')],
    hiddenimports=['babel.numbers', 'phantoms.catphan'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PyLinacGUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['app.ico'],
)
