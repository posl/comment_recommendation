def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        a, b = input().split()
        s.append(a)
        t.append(b)
    for i in range(N):
        if s[i] in t:
            print("No")
            return
    print("Yes")
main()
