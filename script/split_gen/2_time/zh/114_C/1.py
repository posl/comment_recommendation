def main():
    s = input()
    s = '0' + s
    ans = 1000
    for i in range(1, len(s) - 2):
        x = int(s[i:i + 3])
        ans = min(ans, abs(x - 753))
    print(ans)
