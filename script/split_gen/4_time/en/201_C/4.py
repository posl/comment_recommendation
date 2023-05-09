def main():
    s = input()
    ans = 0
    for i in range(10000):
        t = str(i).zfill(4)
        for j in range(10):
            if s[j] == "o" and str(j) not in t:
                break
            if s[j] == "x" and str(j) in t:
                break
        else:
            ans += 1
    print(ans)
