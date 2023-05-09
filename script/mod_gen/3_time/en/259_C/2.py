def main():
    s = input()
    t = input()
    if len(s) > len(t):
        print("No")
        return
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(s):
        print("Yes")
    else:
        print("No")
main()
Python 3.8.2 (default, Mar 26 2020, 15:48:22) [GCC 9.3.0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> import sys >>> sys.version_info # sys.version_info(major=3, minor=8, micro=2, releaselevel='final', serial=0) >>> exit()

if __name__ == '__main__':
    main()