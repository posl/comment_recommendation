def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l-3):
        for j in range(i+3,l):
            if int(s[i:j+1])%2019 == 0:
                ans += 1
    print(ans)
