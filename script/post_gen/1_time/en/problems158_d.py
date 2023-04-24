Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    rev = False
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            rev = not rev
        else:
            if t[1] == '1':
                if rev:
                    s += t[2]
                else:
                    s = t[2] + s
            else:
                if rev:
                    s = t[2] + s
                else:
                    s += t[2]
    if rev:
        print(s[::-1])
    else:
        print(s)

=======
Suggestion 2

def main():
    s = input()
    q = int(input())
    rev = False
    for i in range(q):
        t = list(map(str, input().split()))
        if t[0] == '1':
            rev = not rev
        else:
            if t[1] == '1':
                if rev:
                    s += t[2]
                else:
                    s = t[2] + s
            else:
                if rev:
                    s = t[2] + s
                else:
                    s += t[2]
    if rev:
        print(s[::-1])
    else:
        print(s)

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    rev = False
    head = []
    tail = []
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            rev = not rev
        else:
            if query[1] == "1":
                if rev:
                    tail.append(query[2])
                else:
                    head.append(query[2])
            else:
                if rev:
                    head.append(query[2])
                else:
                    tail.append(query[2])
    if rev:
        print("".join(tail[::-1]) + s[::-1] + "".join(head[::-1]))
    else:
        print("".join(head) + s + "".join(tail))

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    rev = False
    front = []
    back = []
    for i in range(Q):
        query = list(input().split())
        if query[0] == '1':
            rev = not rev
        else:
            if (query[1] == '1') ^ rev:
                front.append(query[2])
            else:
                back.append(query[2])
    front = ''.join(front)
    back = ''.join(back)
    if rev:
        print(back[::-1] + S[::-1] + front[::-1])
    else:
        print(front + S + back)

=======
Suggestion 5

def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        t = input()
        if t == "1":
            T.append(1)
        else:
            f, c = t.split()
            T.append(2)
            F.append(int(f))
            C.append(c)
    rev = 0
    ans = []
    for i in range(Q):
        if T[i] == 1:
            rev ^= 1
        else:
            if (rev + F[i]) % 2 == 0:
                ans.append(C[i])
            else:
                ans.insert(0, C[i])
    if rev == 0:
        print("".join(ans) + S)
    else:
        print("".join(ans[::-1]) + S[::-1])

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        T.append(list(map(str, input().split())))
        if len(T[i]) == 2:
            F.append(T[i][0])
            C.append(T[i][1])
    if F.count('1') % 2 == 0:
        S = S[::-1]
    S = S.replace(' ', '')
    for i in range(Q):
        if len(T[i]) == 1:
            S = S[::-1]
        else:
            if F[i] == '1':
                S = C[i] + S
            else:
                S = S + C[i]
    print(S)

=======
Suggestion 7

def main():
  s = input()
  q = int(input())
  t = [0] * q
  f = [0] * q
  c = [''] * q
  for i in range(q):
    t[i], *f[i:], c[i] = input().split()
    f[i] = int(f[i])
  ans = ''
  rev = False
  for i in range(q):
    if t[i] == '1':
      rev = not rev
    else:
      if rev == (f[i] == 1):
        ans += c[i]
      else:
        ans = c[i] + ans
  if rev:
    ans = ans[::-1]
  print(ans)

=======
Suggestion 8

def main():
    S = input()
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    queries.reverse()

    rev = False
    for query in queries:
        if query[0] == '1':
            rev = not rev
        else:
            if (query[1] == '1') ^ rev:
                S = query[2] + S
            else:
                S = S + query[2]
    if rev:
        S = S[::-1]
    print(S)

=======
Suggestion 9

def main():
    S = input()
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(input().split())
    ans = ""
    for q in query[::-1]:
        if q[0] == "1":
            S = S[::-1]
        else:
            if q[1] == "1":
                S = q[2] + S
            else:
                S = S + q[2]
    print(S)

=======
Suggestion 10

def main():
    #read input
    s = input()
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(input().split())
    #process
    #operations:
    #1: reverse
    #2: add to beginning
    #3: add to end
    #4: do nothing
    #initially, do nothing
    operation = 4
    #initially, empty string
    result = ""
    #for each query
    for query in queries:
        #if operation is 1 or 2
        if operation == 1 or operation == 2:
            #if query is 1
            if query[0] == '1':
                #reverse
                operation = 3 - operation
            #if query is 2
            else:
                #if query is 1
                if query[1] == '1':
                    #add to beginning
                    result += query[2]
                #if query is 2
                else:
                    #add to end
                    result = query[2] + result
        #if operation is 3 or 4
        else:
            #if query is 1
            if query[0] == '1':
                #reverse
                operation = 7 - operation
            #if query is 2
            else:
                #if query is 1
                if query[1] == '1':
                    #add to beginning
                    result = query[2] + result
                #if query is 2
                else:
                    #add to end
                    result += query[2]
    #if operation is 1 or 2
    if operation == 1 or operation == 2:
        #reverse
        result = result[::-1]
    #if operation is 3 or 4
    else:
        #do nothing
        pass
    #output
    print(result)

main()
