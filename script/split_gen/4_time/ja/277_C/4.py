def main():
    n = int(input())
    ab = []
    for _ in range(n):
        a,b = map(int, input().split())
        ab.append((a,b))
    ab.sort(key=lambda x:x[1])
    ans = 0
    for i in range(n):
        if i == 0:
            ans = ab[i][1]
        else:
            if ab[i][0] <= ans:
                ans = ab[i][0]
            else:
                ans = ab[i][1]
    print(ans)
