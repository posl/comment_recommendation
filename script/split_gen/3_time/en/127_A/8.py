def main():
    #input
    a,b = map(int, input().split())
    #output
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(int(b/2))
    else:
        print(0)
main()
Python 3.4.3 (default, Nov 17 2016, 01:08:31) [GCC] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.version
'3.4.3 (default, Nov 17 2016, 01:08:31) [GCC]'
>>> sys.version_info
sys.version_info(major=3, minor=4, micro=3, releaselevel='final', serial=0)
>>>
import sys
print(sys.version)
print(sys.version_info)
