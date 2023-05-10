def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n, 0, -1):
        if a[i-1] == 1:
            ans.append(i)
            for j in range(i-1, 0, -1):
                if j % i == 0:
                    if a[j-1] == 1:
                        a[j-1] = 0
                    else:
                        a[j-1] = 1
    print(len(ans))
    if len(ans) != 0:
        print(*ans)
