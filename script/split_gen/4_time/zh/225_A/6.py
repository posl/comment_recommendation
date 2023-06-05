def main():
    s = input()
    n = len(s)
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    print(ans)
