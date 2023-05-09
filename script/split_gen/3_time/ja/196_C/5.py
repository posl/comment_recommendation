def main():
    N = int(input())
    ans = 0
    for i in range(1, 10**6):
        s = str(i)
        if len(s) % 2 == 0:
            if int(s[:len(s)//2]) <= N:
                ans += 1
    print(ans)
