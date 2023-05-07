def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(x, '-', sep='')
    elif y <= 6:
        print(x)
    elif y <= 9:
        print(x, '+', sep='')
main()
Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=3, releaselevel='final', serial=0)
>>> sys.version
'3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0]'
