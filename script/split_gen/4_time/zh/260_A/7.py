def func(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            print(s[i])
            return
    print("-1")
s = input()
func(s)
