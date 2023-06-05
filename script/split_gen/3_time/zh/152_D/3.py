def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 10 == 0:
            continue
        s = str(i)
        a = int(s[0])
        b = int(s[len(s)-1])
        if a > b:
            continue
        for j in range(1, N+1):
            if j % 10 == 0:
                continue
            if a == j % 10 and b == int(str(j)[0]):
                ans += 1
    print(ans)
