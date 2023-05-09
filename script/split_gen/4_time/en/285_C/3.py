def main():
    inp = input()
    l = len(inp)
    ans = 0
    for i in range(l):
        ans += (ord(inp[i]) - 64) * (26 ** (l - 1 - i))
    print(ans)
