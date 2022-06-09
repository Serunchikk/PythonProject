import os
import platform
import subprocess
my_system = platform.uname()
print(f"System: {my_system.system}")
print(f"Release: {my_system.release}")
print(f"Node Name: {my_system.node}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")


global comands
comands = ['--keyboard','--mouse','--monitor','--gfxcard','--sound','--storage']
comand = 'lshw '
def devices():
    answer = input('Вывести полную информацию? ')
    if answer == 'yes' or answer == 'y':
        for i in comands:
            # print(os.popen(f'{comand}{i}').read())
            try:
                out = subprocess.getoutput(f'{comand}')
            except Exception as e:
                print('Error occured: ', e)
            else:
                print(out)
    else:
        for i in comands:
            # print(os.popen(f'{comand} --short {i}').read())
            try:
                out = subprocess.getoutput(f'{comand} --short {i}')
            
            except Exception as e:
                print('Error occured: ', e)
            else:
                print(out)


devices()