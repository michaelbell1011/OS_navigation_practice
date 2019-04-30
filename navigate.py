import os

def dir_up():
    os.chdir(os.path.dirname(os.getcwd()))

def cwd():
    print(f'cwd: {os.getcwd()}')

def cd():
    cmd = input("change directory command: ")
    if cmd == "cd":
        os.chdir(os.environ.get('HOME')) # navigate to Home dir
        cwd()
    elif cmd == "..":
        dir_up()
        cwd()
    else:
        try:
            os.chdir(os.path.join(os.getcwd(), cmd))
            cwd()
        except Exception:
            print('cd command was not accepted.')

def ls():
    cwd()
    print(f'{os.listdir()}')
