def main():
    s = input()
    n = len(s)
    ans = 753 - int(s[:3])
    for i in range(n-2):
        ans = min(ans, abs(753 - int(s[i:i+3])))
    print(ans)
