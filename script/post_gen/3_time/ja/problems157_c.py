Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if N == 1:
        for i in range(M):
            if s[i] == 1 and c[i] == 0:
                print(-1)
                return
            else:
                print(c[i])
                return
    elif N == 2:
        for i in range(M):
            if s[i] == 1 and c[i] == 0:
                print(-1)
                return
        for i in range(10):
            for j in range(10):
                for k in range(M):
                    if s[k] == 1 and c[k] == i:
                        break
                    elif s[k] == 2 and c[k] == j:
                        break
                else:
                    print(i * 10 + j)
                    return
        print(-1)
    elif N == 3:
        for i in range(M):
            if s[i] == 1 and c[i] == 0:
                print(-1)
                return
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(M):
                        if s[l] == 1 and c[l] == i:
                            break
                        elif s[l] == 2 and c[l] == j:
                            break
                        elif s[l] == 3 and c[l] == k:
                            break
                    else:
                        print(i * 100 + j * 10 + k)
                        return
        print(-1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    for i in range(10 ** N):
        for j in range(M):
            if int(str(i)[s[j] - 1]) != c[j]:
                break
        else:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        else:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        elif M == 1:
            if s[0] == 1:
                print(c[0] * 10)
            elif s[0] == 2:
                print(c[0] + 10)
            else:
                print(-1)
        else:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(c[0] * 10 + c[1])
                else:
                    print(-1)
            else:
                print(-1)
    else:
        if M == 0:
            print(100)
        elif M == 1:
            if s[0] == 1:
                print(c[0] * 100)
            elif s[0] == 2:
                print(c[0] * 10 + 100)
            elif s[0] == 3:
                print(c[0] + 100)
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(c[0] * 100 + c[1] * 10)
                else:
                    print(-1)
            elif s[0] == 1 and s[1] == 3:
                if c[0] == c[1]:
                    print(c[0] * 100 + c[1])
                else:
                    print(-1)
            elif s[0] == 2 and s[1] == 3:
                if c[0] == c[1]:
                    print(c[0] * 10 + c[1] + 100)
                else:
                    print(-1)
            else:

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        else:
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
        return
    if N == 2:
        if M == 0:
            print(10, 11, sep='

')
        else:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(10 * C[0], 10 * C[0] + 1, sep='

')
            elif S[0] == 2:
                if C[0] == 0:
                    print(-1)
                else:
                    print(10 + C[0], 10 + C[0], sep='

')
            else:
                print(-1)
        return
    if N == 3:
        if M == 0:
            print(100, 101, 102, 103, 104, 105, 106, 107, 108, 109, sep='

')
        else:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(100 * C[0], 100 * C[0] + 1, 100 * C[0] + 2, 100 * C[0] + 3, 100 * C[0] + 4, 100 * C[0] + 5, 100 * C[0] + 6, 100 * C[0] + 7, 100 * C[0] + 8, 100 * C[0] + 9, sep='

')
            elif S[0] == 2:
                if C[0] == 0:
                    print(-1)
                else:
                    print(10 + C[0], 10 + C[0], sep='

')
            elif S[0] == 3:
                if C[0]

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
            return
        else:
            if S[0] == 1:
                print(C[0])
                return
            else:
                print(-1)
                return
    elif N == 2:
        if M == 0:
            print(10)
            return
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 10)
                return
            elif S[0] == 2:
                print(C[0] + 10)
                return
            else:
                print(-1)
                return
        else:
            if S[0] == 1:
                if S[1] == 2:
                    if C[0] == C[1]:
                        print(C[0] * 10 + C[1])
                        return
                    else:
                        print(-1)
                        return
                else:
                    print(-1)
                    return
            elif S[0] == 2:
                if S[1] == 1:
                    if C[0] == C[1]:
                        print(C[0] * 10 + C[1])
                        return
                    else:
                        print(-1)
                        return
                else:
                    print(-1)
                    return
            else:
                print(-1)
                return
    else:
        if M == 0:
            print(100)
            return
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 100)
                return
            elif S[0] == 2:
                print(C[0] * 10 + 100)
                return
            elif S[0] == 3:
                print(C[0] + 100)
                return
            else:
                print(-1)
                return
        elif M == 2:
            if S[0] == 1:
                if S[1] == 2:
                    if S[2] == 3:
                        if C[0]

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        a, b = map(int, input().split())
        s.append(a)
        c.append(b)
    if n == 1:
        if m == 0:
            print(0)
        else:
            if c[0] == 0:
                print(-1)
            else:
                print(c[0])
    elif n == 2:
        if m == 0:
            print(10, 11, sep=" ")
        elif m == 1:
            if s[0] == 1:
                if c[0] == 0:
                    print(10, 11, sep=" ")
                else:
                    print(c[0]*10, c[0]*10+1, sep=" ")
            else:
                if c[0] == 0:
                    print(-1)
                else:
                    print(c[0], c[0]+10, sep=" ")
        else:
            if s[0] == 1:
                if c[0] == 0:
                    print(-1)
                else:
                    if s[1] == 2:
                        if c[1] == 0:
                            print(-1)
                        else:
                            print(c[0]*10+c[1])
                    else:
                        print(-1)
            else:
                if c[0] == 0:
                    print(-1)
                else:
                    if s[1] == 2:
                        if c[1] == 0:
                            print(-1)
                        else:
                            print(c[0]+c[1]*10)
                    else:
                        print(-1)
    elif n == 3:
        if m == 0:
            print(100, 101, 102, 103, 104, 105, 106, 107, 108, 109, sep=" ")
        elif m == 1:
            if s[0] == 1:
                if c[0] == 0:
                    print(-1)
                else:
                    print(c[0]*100, c[0]*100+1, c[0]*100+2, c[0]*100+3, c[0]*100+4, c[0]*100+5, c[0

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i],c[i] = map(int,input().split())
    if m == 0:
        if n == 1:
            print(0)
        else:
            print(10**(n-1))
    else:
        if n == 1:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
        else:
            if s[0] == 1:
                if c[0] == 0:
                    print(-1)
                else:
                    for i in range(n-1):
                        print(c[0],end="")
                    for i in range(m-1):
                        print(c[i+1],end="")
                    print()
            else:
                for i in range(n):
                    print(1,end="")
                for i in range(m):
                    print(c[i],end="")
                print()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    c = [0] * N
    for i in range(M):
        s, cc = map(int, input().split())
        if c[s-1] == 0:
            c[s-1] = cc
        elif c[s-1] != cc:
            print(-1)
            return
    if c[0] == 0:
        if N == 1:
            print(0)
        else:
            print(1, end='')
            for i in range(N-1):
                print(0, end='')
            print()
    else:
        if c[0] == 1 and N > 1:
            print(1, end='')
            for i in range(N-1):
                print(0, end='')
            print()
        elif c[0] == 1 and N == 1:
            print(1)
        else:
            print(c[0], end='')
            for i in range(1, N):
                print(c[i], end='')
            print()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s_c = [list(map(int, input().split())) for _ in range(m)]
    #print(n, m, s_c)

    #条件を満たす 0 以上の整数が存在すれば、それらのうち最小のものを出力してください。そのような整数が存在しなければ、 -1と出力してください。
    #十進表記で丁度 N 桁である。(0 は 1 桁の整数とする。その他の整数については、先頭に 0 をつけた表記は認めない。)
    #左から数えて s_i 桁目は c_i である。(i = 1, 2, ..., M)

    #N = 3
    #M = 3
    #s_c = [[1, 7], [3, 2], [1, 7]]

    #N = 3
    #M = 2
    #s_c = [[2, 1], [2, 3]]

    #N = 3
    #M = 1
    #s_c = [[1, 0]]

    #N = 3
    #M = 0
    #s_c = []

    #N = 1
    #M = 0
    #s_c = []

    #N = 1
    #M = 1
    #s_c = [[1, 7]]

    #N = 1
    #M = 2
    #s_c = [[1, 7], [1, 7]]

    #N = 1
    #M = 3
    #s_c = [[1, 7], [1, 7], [1, 7]]

    #N = 1
    #M = 4
    #s_c = [[1, 7], [1, 7], [1, 7], [1, 7]]

    #N = 1
    #M = 5
    #s_c = [[1, 7], [1, 7], [1

=======
Suggestion 10

def main():
  N, M = map(int, input().split())
  L = []
  for i in range(M):
    L.append(list(map(int, input().split())))
  #print(L)
  if M == 0:
    if N == 1:
      print(0)
    else:
      print(10**(N-1))
    return
  for i in range(10**(N-1), 10**N):
    i = str(i)
    for j in range(M):
      if int(i[L[j][0]-1]) != L[j][1]:
        break
    else:
      print(i)
      return
  print(-1)
