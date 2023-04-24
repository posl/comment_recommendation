Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    for i in range(M):
        if A[i] < total / (4 * M):
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[M-1] >= sum(A)/(4*M):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[M-1] >= sum(A) / (4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #N, M = 12, 3
    #A = [4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789]
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total/(4*M):
        print("Yes")
    else:
        print("No")

main()

import sys
import math
import itertools
import collections
import heapq
import operator
import functools
import copy
import bisect
import string
import re
import random

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[-M] >= sum(A) / (4 * M):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] * 4 * m >= total:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort(reverse=True)
  total = sum(a)
  if a[m-1] >= total / (4 * m):
    print("Yes")
  else:
    print("No")

main()

=======
Suggestion 8

def main():
  #N, M = map(int, input().split())
  #A = list(map(int, input().split()))
  N, M = 3, 2
  A = [380, 19, 1]
  #N, M = 12, 3
  #A = [4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789]
  A.sort(reverse=True)
  if A[M-1] >= sum(A)*1/(4*M):
    print('Yes')
  else:
    print('No')

main()

=======
Suggestion 9

def main():
    # Read the input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Sort the input
    A.sort(reverse=True)
    # Check if M popular items can be selected
    if A[M-1] >= sum(A) / (4*M):
        print("Yes")
    else:
        print("No")
