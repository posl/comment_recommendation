def main():
    n = int(input())
    ab = []
    for i in range(n):
        a,b = map(int, input().split())
        ab.append([a,b])
    ab.sort(key=lambda x:x[1])
    #print(ab)
    ans = 0
    for i in range(n):
        if i == 0:
            ans = ab[i][1]
            continue
        if ab[i][0] <= ans:
            continue
        ans = ab[i][1]
    print(ans)
