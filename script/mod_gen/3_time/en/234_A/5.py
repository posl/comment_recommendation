def f(x):
    return x*x+2*x+3
t = int(input())
print(f(f(f(t)+t)+f(f(t))))
Python 3.8.2 (default, Mar  6 2021, 16:33:27) 
[GCC 10.2.1 20201203] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
 RESTART: /home/bruno/Documentos/Python/Python/Python/

if __name__ == '__main__':
    f()