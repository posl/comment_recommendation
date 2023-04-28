Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    dic = {}
    for i in range(26):
        dic[x[i]] = chr(ord("a") + i)
    s.sort(key=lambda x: "".join([dic[c] for c in x]))
    for i in range(n):
        print(s[i])

=======
Suggestion 2

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
Suggestion 3

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    table = {}
    for i in range(len(x)):
        table[x[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(table))
    s = sorted(s)
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(dict(map(reversed, table.items()))))
    for i in range(n):
        print(s[i])

=======
Suggestion 4

def main():
    # input
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    # compute
    d = {}
    for i in range(26):
        d[x[i]] = chr(i+97)

    for i in range(n):
        for j in range(len(s[i])):
            s[i] = s[i].replace(s[i][j], d[s[i][j]])

    # output
    for i in sorted(s):
        print(i)

=======
Suggestion 5

def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort(key=lambda s: [X.find(c) for c in s])
    print('\n'.join(S))

=======
Suggestion 6

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(x)
    #print(n)
    #print(s)
    order = []
    for i in range(len(x)):
        order.append(x[i])
    #print(order)
    order.sort()
    #print(order)
    #print(order.index('z'))
    #print(order.index('a'))
    #print(order.index('b'))
    #print(order.index('c'))
    #print(order.index('d'))
    #print(order.index('e'))
    #print(order.index('f'))
    #print(order.index('g'))
    #print(order.index('h'))
    #print(order.index('i'))
    #print(order.index('j'))
    #print(order.index('k'))
    #print(order.index('l'))
    #print(order.index('m'))
    #print(order.index('n'))
    #print(order.index('o'))
    #print(order.index('p'))
    #print(order.index('q'))
    #print(order.index('r'))
    #print(order.index('s'))
    #print(order.index('t'))
    #print(order.index('u'))
    #print(order.index('v'))
    #print(order.index('w'))
    #print(order.index('x'))
    #print(order.index('y'))
    #print(order.index('z'))
    #print(order.index('a'))
    #print(order.index('b'))
    #print(order.index('c'))
    #print(order.index('d'))
    #print(order.index('e'))
    #print(order.index('f'))
    #print(order.index('g'))
    #print(order.index('h'))
    #print(order.index('i'))
    #print(order.index('j'))
    #print(order.index('k'))
    #print(order.index('l'))
    #print(order.index('m'))
    #print(order.index('n'))
    #print(order.index('o'))
    #print(order.index('p'))
    #print(order.index('q'))
    #print(order.index('r'))
    #print(order.index('s'))
    #print(order.index('t'))
    #print(order.index('u'))
    #print(order.index('v'))
    #print(order.index('w'))
    #print(order.index('x'))
    #print(order.index('y'))
    #print(order.index('z'))

=======
Suggestion 7

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [x.translate(str.maketrans(x, x, x)) for x in 'zyxwvutsrqponmlkjihgfedcba'.translate(str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz'))])
    print("\n".join(s))

=======
Suggestion 8

def main():
    x = input()
    n = int(input())
    s = [input() for i in range(n)]
    #print(x)
    #print(n)
    #print(s)
    xlist = list(x)
    xdict = {}
    for i in range(len(xlist)):
        xdict[xlist[i]] = chr(i+97)
    #print(xdict)
    sdict = {}
    for i in range(n):
        slist = list(s[i])
        sdict[s[i]] = ''
        for j in range(len(slist)):
            sdict[s[i]] += xdict[slist[j]]
    #print(sdict)
    sdict = sorted(sdict.items(), key=lambda x:x[1])
    #print(sdict)
    for i in range(n):
        print(sdict[i][0])

=======
Suggestion 9

def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    #print(X)
    #print(N)
    #print(S)
    #print( len(S[0]) )

    #X = list('zyxwvutsrqponmlkjihgfedcba')
    #S = ['a','ab','abc','ac','b']

    #X = list('bacdefghijklmnopqrstuvwxzy')
    #S = ['abx','bzz','bzy','caa']

    X = list(X)
    S = sorted(S)

    #print(X)
    #print(S)

    X_dic = {}
    for i in range(len(X)):
        X_dic[X[i]] = i

    #print(X_dic)

    S_dic = {}
    for s in S:
        tmp = []
        for i in range(len(s)):
            tmp.append( X_dic[s[i]] )
        S_dic[s] = tmp

    #print(S_dic)

    S_dic_sorted = sorted(S_dic.items(), key=lambda x:x[1])

    #print(S_dic_sorted)

    for s in S_dic_sorted:
        print(s[0])

main()

=======
Suggestion 10

def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    #print(s)
    #print(x)
    x_dict = {}
    for i in range(len(x)):
        x_dict[x[i]] = chr(ord('a') + i)
    #print(x_dict)
    s_dict = {}
    for i in range(n):
        tmp = ''
        for j in range(len(s[i])):
            tmp += x_dict[s[i][j]]
        s_dict[tmp] = s[i]
    #print(s_dict)
    s_dict = sorted(s_dict.items())
    #print(s_dict)
    for i in range(n):
        print(s_dict[i][1])
