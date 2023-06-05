def func(n, s, a, b):
    for i in range(n):
        if a[i] == s or b[i] == s:
            print("Yes")
            print("T" * i + "H" + "T" * (n - i - 1))
            return
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == s or a[i] + b[j] == s or b[i] + a[j] == s or b[i] + b[j] == s:
                print("Yes")
                if a[i] + a[j] == s:
                    print("T" * i + "TT" + "T" * (j - i - 1) + "H" + "T" * (n - j - 1))
                    return
                if a[i] + b[j] == s:
                    print("T" * i + "TH" + "T" * (j - i - 1) + "T" * (n - j - 1))
                    return
                if b[i] + a[j] == s:
                    print("T" * i + "HT" + "T" * (j - i - 1) + "T" * (n - j - 1))
                    return
                if b[i] + b[j] == s:
                    print("T" * i + "HH" + "T" * (j - i - 1) + "T" * (n - j - 1))
                    return
    print("No")
n, s = map(int, input().split())
a = []
b = []
for i in range(n):
    ta, tb = map(int, input().split())
    a.append(ta)
    b.append(tb)
func(n, s, a, b)
