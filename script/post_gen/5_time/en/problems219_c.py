Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda s: [x.index(c) for c in s])
    print(*s, sep='\n')

=======
Suggestion 2

def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort(key=lambda s: [X.index(x) for x in s])
    for s in S:
        print(s)

=======
Suggestion 3

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(0,n):
        s.append(input())

    x_dict = {}
    for i in range(0,26):
        x_dict[x[i]] = chr(ord('a')+i)

    for i in range(0,n):
        for j in range(0,len(s[i])):
            s[i] = s[i].replace(s[i][j],x_dict[s[i][j]])

    s.sort()
    for i in range(0,n):
        for j in range(0,len(s[i])):
            s[i] = s[i].replace(s[i][j],x[j])
    for i in range(0,n):
        print(s[i])

main()

=======
Suggestion 4

def main():
    new_order = input()
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    new_order_dict = {}
    for i in range(26):
        new_order_dict[new_order[i]] = chr(ord('a')+i)
    for i in range(n):
        s = ''
        for j in range(len(names[i])):
            s += new_order_dict[names[i][j]]
        names[i] = s
    names.sort()
    for i in range(n):
        s = ''
        for j in range(len(names[i])):
            s += new_order[new_order_dict[names[i][j]]]
        names[i] = s
    for i in range(n):
        print(names[i])

=======
Suggestion 5

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    x = sorted(x)
    for i in range(n):
        s[i] = sorted(s[i], key=x.index)
    s = sorted(s)
    for i in range(n):
        print(''.join(s[i]))

=======
Suggestion 6

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [x.translate(str.maketrans(x,x[::-1])),x])
    for i in range(n):
        print(s[i])

=======
Suggestion 7

def solve():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    D = dict()
    for i in range(26):
        D[X[i]] = chr(i+97)
    for i in range(N):
        S[i] = "".join([D[x] for x in S[i]])
    S.sort()
    for i in range(N):
        S[i] = "".join([X[ord(x)-97] for x in S[i]])
    print("\n".join(S))
solve()

=======
Suggestion 8

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    x = list(x)
    y = []
    for i in range(26):
        y.append(chr(ord('a') + i))
    d = {}
    for i in range(26):
        d[y[i]] = x[i]
    for i in range(n):
        s[i] = list(s[i])
        for j in range(len(s[i])):
            s[i][j] = d[s[i][j]]
        s[i] = ''.join(s[i])
    s.sort()
    for i in range(n):
        for j in range(len(s[i])):
            s[i][j] = d[s[i][j]]
        s[i] = ''.join(s[i])
    for i in range(n):
        print(s[i])

=======
Suggestion 9

def solve():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda s: ''.join(map(lambda c: chr(x.index(c) + 97), s)))
    print('\n'.join(s))
solve()

=======
Suggestion 10

def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    x_dic = {x[i]: chr(97 + i) for i in range(len(x))}
    s.sort(key=lambda x: ''.join([x_dic[x[i]] for i in range(len(x))]))
    print(*s, sep='\n')
