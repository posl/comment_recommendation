def main():
    s = input()
    o = s.count("o")
    x = s.count("x")
    q = s.count("?")
    ans = 0
    for i in range(10000):
        c = 0
        for j in range(4):
            if s[int(str(i).zfill(4)[j])] == "o":
                c += 1
            elif s[int(str(i).zfill(4)[j])] == "x":
                c = 0
                break
        if c == o and 4 - c - q == x:
            ans += 1
    print(ans)
