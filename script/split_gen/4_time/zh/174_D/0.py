def main():
    n = int(input())
    c = input()
    cnt = 0
    for i in range(n):
        if c[i] == "W":
            cnt += 1
    ans = 0
    for i in range(cnt):
        if c[i] == "R":
            ans += 1
    print(ans)
