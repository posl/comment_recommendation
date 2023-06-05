def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
