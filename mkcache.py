import os
import time

from navigate import dir_up, cwd, cd, ls

def go_home():
    os.chdir(os.environ.get('HOME')) # navigate to Home dir
    cwd()

def go_desktop():
    os.chdir(os.path.join(os.environ.get('HOME'), 'Desktop'))  # navigate to Desktop
    cwd()
    
def mk_cache(): 
# create a testing directory with subdirectory named by the timestamp it was created
    go_desktop()
    timestamp = time.ctime()
    os.makedirs(f'cache/{timestamp}')
    os.chdir(f'cache/{timestamp}')  # navigates to new timestamp directory
    cwd()

def rm_files():
    for file in os.listdir(os.getcwd()):
        os.remove(file)

def rm_cache_subdirs():
    for subdir in os.listdir('cache'):
        full_path = os.path.join(os.getcwd(), 'cache', subdir)
        os.chdir(full_path)  # enter subdir
        rm_files()  # delete files
        go_desktop()
        os.rmdir(full_path)  # delete empty subdir
    
def rm_cache():
# from the Desktop delete the created testing directories
    if os.path.exists(os.path.join(os.environ.get('HOME'), 'Desktop', 'cache')):
        if input('Delete cache? [y or n]: ').lower() == 'y':
            go_desktop()
            rm_cache_subdirs()
            os.rmdir('cache')
            print('cache deleted.')
        else: print('cache not deleted.')
    else: print('cache not set up.')



