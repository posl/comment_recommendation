def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if "7" in str(i):
            continue
        if "7" in str(oct(i)):
            continue
        ans += 1
    print(ans)
