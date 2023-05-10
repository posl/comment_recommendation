def main():
    import sys
    input = sys.stdin.readline
    import itertools
    from collections import deque
    import bisect
    import heapq
    import math
    import copy
    import collections
    from collections import deque
    from collections import defaultdict
    from collections import Counter
    from functools import reduce
    S1 = input()[:-1]
    S2 = input()[:-1]
    S3 = input()[:-1]
    S = set(S1+S2+S3)
    if len(S)>10:
        print("UNSOLVABLE")
        exit()
    S = list(S)
    if len(S)>10:
        print("UNSOLVABLE")
        exit()
    if len(S)==10:
        for i in range(10):
            S[i] = str(i)
    else:
        for i in range(len(S)):
            S[i] = str(i)
    S = "".join(S)
    for i in range(10**(len(S1)-1),10**len(S1)):
        N1 = str(i)
        if len(set(N1))!=len(N1):
            continue
        for j in range(10**(len(S2)-1),10**len(S2)):
            N2 = str(j)
            if len(set(N2))!=len(N2):
                continue
            for k in range(10**(len(S3)-1),10**len(S3)):
                N3 = str(k)
                if len(set(N3))!=len(N3):
                    continue
                if int(N1)+int(N2)==int(N3):
                    dic = {}
                    for l in range(len(S1)):
                        dic[S1[l]] = N1[l]
                    for l in range(len(S2)):
                        dic[S2[l]] = N2[l]
                    for l in range(len(S3)):
                        dic[S3[l]] = N3[l]
                    if dic[S1[0]]=="0" or dic[S2[0]]=="0" or dic[S3[0]]=="0":
                        continue
                    for l in range(len(S1)):
                        S1 = S1.replace(S1[l],dic[S1[l]])
                    for l in range(len(S2)):
                        S2 = S2.replace(S2[l],dic[S2[l]])
                    for l in range(len(S3)):
                        S3 = S3

if __name__ == '__main__':
    main()