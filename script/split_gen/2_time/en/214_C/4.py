def main():
    n = int(input())
    s = [int(i) for i in input().split()]
    t = [int(i) for i in input().split()]
    ans = []
    for i in range(n):
        ans.append(t[i])
    for i in range(n):
        for j in range(n):
            if ans[(i+j)%n] > ans[i%n] + s[(i+j)%n]:
                ans[(i+j)%n] = ans[i%n] + s[(i+j)%n]
    for i in range(n):
        print(ans[i])
