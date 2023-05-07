def main():
    import sys
    import re
    import math
    k = int(sys.stdin.readline().rstrip())
    if k%2 == 0 or k%5 == 0:
        print(-1)
    else:
        n = 7
        count = 1
        while n%k != 0:
            n = n*10 + 7
            count += 1
        print(count)
main()
I got a TLE, but I was able to solve the problem.
The following code was my first submission.

if __name__ == '__main__':
    main()