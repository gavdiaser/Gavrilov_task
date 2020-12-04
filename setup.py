from cx_Freeze import setup, Executable

executables = [Executable('tensor_task.py',
targetName='D:\\server\\Gavrilov_task\\Gavrilov_task.exe')]


includes = ['urllib', 'bs4', 'os']

zip_include_packages = ['urllib', 'bs4', 'os']

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
}
}

setup(name='tensor_task',
version='0.0.1',
description='URLToText',
executables=executables,
options=options)