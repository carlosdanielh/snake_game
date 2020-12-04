import cx_Freeze

executables = [cx_Freeze.Executable('snakeultimo.py',base = 'Win32GUI')]
build_exe_options = {'packages':['pygame'],
         'include_files':['comer.ogg','dragons.ogg','gameover.ogg',
                          'intro.ogg','pausa.ogg','gameoverfinal.jpg',
                          'iconos.png','inicio.jpg','pausar.png',
                          'backgroundsnake.jpg']}

cx_Freeze.setup(
    name = 'snakeultimo',
    version = '1.0',
    description = 'juego snake version 1',
    options = {'build_exe': build_exe_options},
    executables = executables
    )
    
