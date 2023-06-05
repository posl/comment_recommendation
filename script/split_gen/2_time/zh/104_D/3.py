def main():
    s = input()
    q = s.count("?")
    ans = 1
    for i in range(1,q+1):
        ans *= 3
        ans %= 1000000007
    print(ans)
