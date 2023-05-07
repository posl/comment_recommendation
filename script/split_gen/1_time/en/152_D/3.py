def main():
    N = int(input())
    D = [0] * 100
    for i in range(1, N + 1):
        s = str(i)
        D[int(s[0]) * 10 + int(s[-1])] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += D[i * 10 + j] * D[j * 10 + i]
    print(ans)
main()
