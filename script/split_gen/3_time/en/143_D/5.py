def main():
    n = int(input())
    l = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] != l[k]:
                    if l[i] + l[j] > l[k]:
                        ans += 1
    print(ans)
