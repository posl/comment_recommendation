Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(max(set(s), key=s.count))

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(max(s,key=s.count))

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    d = {}
    for name in S:
        if name in d:
            d[name] += 1
        else:
            d[name] = 1

    max = 0
    max_name = ''
    for name in d:
        if d[name] > max:
            max = d[name]
            max_name = name

    print(max_name)

=======
Suggestion 4

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    print(max(l,key=l.count))

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(max(s, key=s.count))

=======
Suggestion 6

def main():
    n = int(input())
    S = []
    for i in range(n):
        S.append(input())
    S.sort()
    #print(S)
    dic = {}
    for i in S:
        dic[i] = S.count(i)
    #print(dic)
    max_v = max(dic.values())
    for k, v in dic.items():
        if v == max_v:
            print(k)
            break

=======
Suggestion 7

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    print(max(set(name), key=name.count))

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    max = 0
    for i in range(n):
        if s.count(s[i]) > max:
            max = s.count(s[i])
            name = s[i]
    print(name)

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    S.append('')
    max = 0
    max_name = ''
    count = 0
    for i in range(N):
        if S[i] == S[i+1]:
            count += 1
        else:
            if max < count:
                max = count
                max_name = S[i]
            count = 0
    print(max_name)

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(max(s,key=s.count))
main()
