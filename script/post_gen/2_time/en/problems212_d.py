Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    bag = []
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            for j in range(len(bag)):
                bag[j] += int(query[1])
        elif query[0] == '3':
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 2

def main():
    Q = int(input())
    bag = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            bag.append(int(query[1]))
        elif query[0] == '2':
            bag = [x + int(query[1]) for x in bag]
        else:
            print(min(bag))
            bag.remove(min(bag))

=======
Suggestion 3

def main():
    Q = int(input())
    P = []
    X = []
    for _ in range(Q):
        p, *x = map(int, input().split())
        P.append(p)
        X.append(x[0] if x else None)
    #print(P)
    #print(X)
    A = []
    for i in range(Q):
        if P[i] == 1:
            A.append(X[i])
        elif P[i] == 2:
            A = [x + X[i] for x in A]
        else:
            A.sort()
            print(A.pop(0))
    return

main()

=======
Suggestion 4

def main():
    Q = int(input())
    bag = []
    add = 0
    for i in range(Q):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            bag.append(query[1] - add)
        elif query[0] == 2:
            add += query[1]
        else:
            min = 10**9
            for j in range(len(bag)):
                if bag[j] < min:
                    min = bag[j]
                    index = j
            print(min + add)
            bag.pop(index)

=======
Suggestion 5

def main():
    import heapq
    N = int(input())
    q = []
    for _ in range(N):
        p, x = map(int, input().split())
        if p == 1:
            heapq.heappush(q, x)
        elif p == 2:
            q = [x + y for y in q]
            heapq.heapify(q)
        else:
            print(heapq.heappop(q))

main()

The first line is a simple import statement. The second line is a function definition. The third line is a variable definition. The fourth line is a loop definition. The fifth line is a variable definition. The sixth line is a variable definition. The seventh line is a conditional statement. The eighth line is a conditional statement. The ninth line is a conditional statement. The tenth line is a conditional statement. The eleventh line is a conditional statement. The twelfth line is a conditional statement. The thirteenth line is a conditional statement. The fourteenth line is a conditional statement. The fifteenth line is a conditional statement. The sixteenth line is a conditional statement. The seventeenth line is a conditional statement. The eighteenth line is a conditional statement. The nineteenth line is a conditional statement. The twentieth line is a conditional statement. The twenty-first line is a conditional statement. The twenty-second line is a conditional statement. The twenty-third line is a conditional statement. The twenty-fourth line is a conditional statement. The twenty-fifth line is a conditional statement. The twenty-sixth line is a conditional statement. The twenty-seventh line is a conditional statement. The twenty-eighth line is a conditional statement. The twenty-ninth line is a conditional statement. The thirtieth line is a conditional statement. The thirty-first line is a conditional statement. The thirty-second line is a conditional statement. The thirty-third line is a conditional statement. The thirty-fourth line is a conditional statement. The thirty-fifth line is a conditional statement. The thirty-sixth line is a conditional statement. The thirty-seventh line is a conditional statement. The thirty-eighth line is a conditional statement. The thirty-ninth line is a conditional statement. The fortieth line is a conditional statement. The forty-first line is a conditional statement. The forty-second line is a conditional statement. The forty-third line is a conditional statement. The forty-fourth line is a conditional statement. The forty-fifth line is a conditional

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    ans = []
    for i in range(Q):
        P, X = map(int, input().split())
        if P == 1:
            pass
        elif P == 2:
            pass
        else:
            ans.append(X)
    print('

'.join(map(str, ans)))

=======
Suggestion 7

def main():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(query)

    bag = []
    add = 0
    for i in range(Q):
        if query[i][0] == 1:
            bag.append(query[i][1] - add)
        elif query[i][0] == 2:
            add += query[i][1]
        else:
            bag.sort()
            print(bag[0] + add)
            bag.pop(0)

=======
Suggestion 8

def main():
    #input
    Q = int(input())
    PQX = [list(map(int, input().split())) for _ in range(Q)]

    #solve
    ans = [0] * Q
    que = []
    add = 0
    for i, (p, x) in enumerate(PQX):
        if p == 1:
            que.append(x-add)
        elif p == 2:
            add += x
        else:
            ans[i] = min(que) + add
            que.remove(min(que))

    #output
    for i in range(Q):
        if PQX[i][0] == 3:
            print(ans[i])

=======
Suggestion 9

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        a,b = map(int, input().split())
        A.append([a,b])
    
    ans = []
    min = 0
    add = 0
    for i in range(Q):
        if A[i][0] == 1:
            A[i][1] -= add
            if A[i][1] < min:
                min = A[i][1]
        elif A[i][0] == 2:
            add += A[i][1]
        else:
            ans.append(min+add)
            min += add
            add = 0
    for i in ans:
        print(i)

=======
Suggestion 10

def main():
    Q = int(input())
    operations = [list(map(int, input().split())) for i in range(Q)]

    # 1 3
