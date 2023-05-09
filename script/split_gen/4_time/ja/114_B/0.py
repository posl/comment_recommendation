def main():
    s = input()
    ans = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        ans = min(ans, abs(753-x))
    print(ans)
