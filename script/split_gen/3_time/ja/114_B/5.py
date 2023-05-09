def main():
    s = input()
    l = len(s)
    ans = 10**10
    for i in range(l-2):
        x = int(s[i:i+3])
        ans = min(ans, abs(x-753))
    print(ans)
