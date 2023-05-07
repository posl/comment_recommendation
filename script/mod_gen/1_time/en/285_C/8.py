def main():
    import sys
    import math
    import time
    start = time.time()
    s = input()
    #s = 'BRUTMHYHIIZP'
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i])-64) * (26**(len(s)-i-1))
    print(ans)
    elapsed_time = time.time() - start
    #print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    main()