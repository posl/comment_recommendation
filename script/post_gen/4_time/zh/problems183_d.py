Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, w = map(int, input().split())
    #print(n, w)
    #print(type(n), type(w))
    #prin

=======
Suggestion 2

def main():
    n,w = map(int,input().split())
    use = [0]*200000
    for i in range(n):
        s,t,p = map(int,input().split())
        use[s] += p
        use[t] -= p
    for i in range(1,200000):
        use[i] += use[i-1]
        if use[i] > w:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 3

def main():
    N,W = map(int,input().split())
    people = []
    for i in range(N):
        people.append(list(map(int,input().split())))
    people.sort(key=lambda x:x[0])
    people.sort(key=lambda x:x[1])
    #print(people)
    #print('N:',N)
    #print('W:',W)
    #print('people:',people)
    #print('people[0][0]:',people[0][0])
    #print('people[0][1]:',people[0][1])
    #print('people[0][2]:',people[0][2])
    #print('people[1][0]:',people[1][0])
    #print('people[1][1]:',people[1][1])
    #print('people[1][2]:',people[1][2])
    #print('people[2][0]:',people[2][0])
    #print('people[2][1]:',people[2][1])
    #print('people[2][2]:',people[2][2])
    #print('people[3][0]:',people[3][0])
    #print('people[3][1]:',people[3][1])
    #print('people[3][2]:',people[3][2])
    #print('people[4][0]:',people[4][0])
    #print('people[4][1]:',people[4][1])
    #print('people[4][2]:',people[4][2])
    #print('people[5][0]:',people[5][0])
    #print('people[5][1]:',people[5][1])
    #print('people[5][2]:',people[5][2])
    #print('people[6][0]:',people[6][0])
    #print('people[6][1]:',people[6][1])
    #print('people[6][2]:',people[6][2])
    #print('people[7][0]:',people[7][0])
    #print('people[7][1]:',people[7][1])
    #print('people[7][2]:',people[7][2])
    #print('people[8][0

=======
Suggestion 4

def main():
    n, w = map(int, input().split())
    use = [0] * 200001
    for i in range(n):
        s, t, p = map(int, input().split())
        use[s] += p
        use[t] -= p
    for i in range(1, 200001):
        use[i] += use[i-1]
        if use[i] > w:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    n, w = map(int, input().split())
    t = [0] * 200001
    for i in range(n):
        s, e, p = map(int, input().split())
        t[s] += p
        t[e] -= p
    for i in range(1, 200001):
        t[i] += t[i - 1]
        if t[i] > w:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def solve():
    n, w = map(int, input().split())
    a = []
    for _ in range(n):
        s, t, p = map(int, input().split())
        a.append((s, p))
        a.append((t, -p))
    a.sort()
    s = 0
    for _, p in a:
        s += p
        if s > w:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def solve():
    n, w = map(int, input().split())
    d = {}
    for _ in range(n):
        s, t, p = map(int, input().split())
        if s not in d:
            d[s] = 0
        d[s] += p
        if t not in d:
            d[t] = 0
        d[t] -= p
    for k in sorted(d.keys()):
        w -= d[k]
        if w < 0:
            print("No")
            return
    print("Yes")

solve()

=======
Suggestion 8

def main():
    n, w = map(int, input().split())
    events = []
    for i in range(n):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()
    current = 0
    for _, p in events:
        current += p
        if current > w:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 9

def main():
    n,w=map(int,input().split())
    #s=[0]*n
    #t=[0]*n
    #p=[0]*n
    #for i in range(n):
    #    s[i],t[i],p[i]=map(int,input().split())
    #s,t,p=map(list,zip(*sorted(zip(s,t,p))))
    #print(s,t,p)
    #for i in range(n):
    #    if i==0:
    #        if p[i]>w:
    #            print("No")
    #            exit(0)
    #        else:
    #            w-=p[i]
    #    else:
    #        if s[i]-t[i-1]>0:
    #            w+=p[i-1]
    #        if p[i]>w:
    #            print("No")
    #            exit(0)
    #        else:
    #            w-=p[i]
    #print("Yes")

    imos=[0]*(200001)
    for i in range(n):
        s,t,p=map(int,input().split())
        imos[s]+=p
        imos[t]-=p
    for i in range(1,200001):
        imos[i]+=imos[i-1]
        if imos[i]>w:
            print("No")
            exit(0)
    print("Yes")

=======
Suggestion 10

def main():
    n, w = map(int, input().split())
    water = [0] * 200001
    for i in range(n):
        s, t, p = map(int, input().split())
        water[s] += p
        water[t] -= p
    for i in range(200000):
        water[i + 1] += water[i]
        if water[i] > w:
            print("No")
            return
    print("Yes")
