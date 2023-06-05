def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    t = [input() for i in range(h)]
    s = ["".join(s[i]) for i in range(h)]
    t = ["".join(t[i]) for i in range(h)]
    s.sort()
    t.sort()
    if s == t:
        print("Yes")
    else:
        print("No")
