def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    C = [0] * (10**5+1)
    for a in A:
        C[a] += 1
    ans = 0
    for i in range(1, 10**5):
        if C[i] == 0:
            continue
        for j in range(i+1, 10**5+1):
            if C[j] == 0:
                continue
            for k in range(j+1, 10**5+1):
                if C[k] == 0:
                    continue
                ans += C[i] * C[j] * C[k]
    print(ans)

if __name__ == '__main__':
    main()