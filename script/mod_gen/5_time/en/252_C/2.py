def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(10):
        min = 100
        for j in range(N):
            count = 0
            for k in range(10):
                if S[j][k] == str(i):
                    count += 1
            if count < min:
                min = count
        if min > ans:
            ans = min
    print(ans)
main()
