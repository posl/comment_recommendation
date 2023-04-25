Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H - R) * (W - C))

main()

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    ans = 0
    if H != 1:
        ans += W
    if W != 1:
        ans += H
    if H != 1 and W != 1:
        ans -= 1
    print(ans)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(2 * (h - 1) + 2 * (w - 1) - (r == 1) - (r == h) - (c == 1) - (c == w))

=======
Suggestion 4

def solve(h, w, r, c):
    if h == 1 and w == 1:
        return 0
    if h == 1 and w != 1:
        return 2
    if h != 1 and w == 1:
        return 2
    if h != 1 and w != 1:
        return 4

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h - r) + (w - c) + 1)

=======
Suggestion 6

def main():
    # Write your code here
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    if H == 1 and W == 1:
        print(0)
    elif H == 1 or W == 1:
        print(1)
    else:
        print(2)

=======
Suggestion 7

def main():
    # H, W = [int(x) for x in input().split()]
    # R, C = [int(x) for x in input().split()]
    H, W = 3, 4
    R, C = 2, 2
    print((H - 1) * (W - 1) - 1)

=======
Suggestion 8

def main():
    H,W=map(int,input().split())
    R,C=map(int,input().split())
    print((H-R)+(W-C))

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h - r) + (w - c) + 1)

main()

import sys
import math
import heapq
import bisect
import random

=======
Suggestion 10

def main():
    #input
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    #output
    print(2 * (H + W) - 4)
