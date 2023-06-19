def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**n):
        bits = []
        for j in range(n):
            if (i >> j) & 1:
                bits.append(j)
        ok = True
        for j in range(len(bits)):
            for k in range(j+1, len(bits)):
                if A[bits[j]][bits[k]] == 0:
                    ok = False
        if ok:
            t = 0
            for j in range(len(bits)):
                t ^= bits[j]
            ans = max(ans, t)
    print(ans)
