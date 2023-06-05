def sort_by_alphabet_order():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # print(x)
    # print(n)
    # print(s)
    s.sort(key=lambda x: [x.replace(c, chr(123 - ord(c))) for c in x])
    # print(s)
    for i in range(n):
        print(s[i])
