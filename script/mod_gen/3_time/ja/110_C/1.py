def main():
    S = input()
    T = input()
    s2t = {}
    t2s = {}
    for s, t in zip(S, T):
        if s in s2t and s2t[s] != t:
            print("No")
            return
        if t in t2s and t2s[t] != s:
            print("No")
            return
        s2t[s] = t
        t2s[t] = s
    print("Yes")

if __name__ == '__main__':
    main()