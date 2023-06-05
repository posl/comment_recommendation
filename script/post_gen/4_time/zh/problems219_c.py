Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    s.sort(key=lambda s: [x.index(c) for c in s])
    for i in range(n):
        print(s[i])

=======
Suggestion 2

def sort_by_new_order(x, y):
    for i in range(len(x)):
        if x[i] != y[i]:
            return new_order.index(x[i]) - new_order.index(y[i])
    return len(x) - len(y)

new_order = input()
n = int(input())
names = []
for i in range(n):
    names.append(input())
names.sort(key = lambda x: sort_by_new_order(x, new_order))
for name in names:
    print(name)

=======
Suggestion 3

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [ord(x[i]) for i in range(len(x))])
    for i in s:
        print(i)

=======
Suggestion 4

def lex_cmp(x, y, order):
    for i in range(0, min(len(x), len(y))):
        if order.index(x[i]) < order.index(y[i]):
            return -1
        elif order.index(x[i]) > order.index(y[i]):
            return 1
    if len(x) < len(y):
        return -1
    elif len(x) > len(y):
        return 1
    else:
        return 0

=======
Suggestion 5

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

=======
Suggestion 6

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    x_dict = {}
    for i in range(26):
        x_dict[x[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = ''.join([x_dict[x] for x in s[i]])
    s.sort()
    for i in range(n):
        print(s[i])

=======
Suggestion 7

def get_order_dict(order):
    order_dict = {}
    for i in range(len(order)):
        order_dict[order[i]] = i
    return order_dict

=======
Suggestion 8

def main():
    x = input()
    n = int(input())
    s = [input() for i in range(n)]
    d = {c: i for i, c in enumerate(x)}
    s.sort(key=lambda x: [d[c] for c in x])
    print(*s, sep='\n')

=======
Suggestion 9

def compare(s1, s2, x):
    if len(s1) < len(s2):
        s1 = s1 + 'a' * (len(s2) - len(s1))
    elif len(s1) > len(s2):
        s2 = s2 + 'a' * (len(s1) - len(s2))
    for i in range(len(s1)):
        if x.index(s1[i]) < x.index(s2[i]):
            return -1
        elif x.index(s1[i]) > x.index(s2[i]):
            return 1
    return 0

x = input()
n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort(cmp=lambda s1, s2:compare(s1, s2, x))
for i in range(n):
    print s[i]
