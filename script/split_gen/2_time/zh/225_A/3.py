def main():
    s = input()
    a = []
    for i in range(3):
        a.append(s[i])
    a.sort()
    ans = 1
    for i in range(2):
        if a[i] != a[i + 1]:
            ans += 1
    print(ans)
