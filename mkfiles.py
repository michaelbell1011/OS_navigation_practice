from mkcache import *

def main():
    mk_cache()

    with open('hi.txt', 'w') as f:
        print(f'{f.name} was created in the above directory.')
        body = "Hello World!"
        f.write(body)


if __name__=="__main__":
    main()
