def main():
    N = int(input())
    ans = 0
    for i in range(1, 10**6+1):
        s = str(i)
        if len(s) % 2 == 0:
            a = s[:len(s)//2]
            b = s[len(s)//2:]
            if a == b:
                ans += 1
    print(ans)
