def main():
    N = input()
    k = len(N)
    ans = -1
    for i in range(1, 1 << k):
        S = ""
        for j in range(k):
            if (i >> j) & 1:
                S += N[j]
        if int(S) % 3 == 0:
            ans = max(ans, k - bin(i).count("1"))
    print(ans)
