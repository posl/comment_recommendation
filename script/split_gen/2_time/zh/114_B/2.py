def main():
    s = input()
    s = list(map(int, s))
    ans = 1000
    for i in range(len(s)-2):
        x = s[i]*100 + s[i+1]*10 + s[i+2]
        ans = min(ans, abs(x-753))
    print(ans)
