def main():
    N = input()
    ans = 0
    for i in range(len(N)):
        if i == 0:
            continue
        a = int(N[:i])
        b = int(N[i:])
        ans = max(ans, a*b)
    print(ans)
