Synthesizing 10/10 solutions

=======
Suggestion 1

def paint(n, a, b, p, q, r, s):
    #print("n:%d, a:%d, b:%d, p:%d, q:%d, r:%d, s:%d" % (n, a, b, p, q, r, s))
    if (p <= a <= q and r <= b <= s):
        return '#'
    if (p <= a <= q and r <= b <= s):

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p,q+1):
        for j in range(r,s+1):
            if (i-a == j-b) or (i-a == b-j):
                print("#",end="")
            else:
                print(".",end="")
        print("")

=======
Suggestion 4

def problem230_c():
    pass

=======
Suggestion 5

def main():
  N, A, B = [int(x) for x in input().split()]
  P, Q, R, S = [int(x) for x in input().split()]
  
  #print(N, A, B)
  #print(P, Q, R, S)
  
  #print("N:", N)
  #print("A:", A)
  #print("B:", B)
  #print("P:", P)
  #print("Q:", Q)
  #print("R:", R)
  #print("S:", S)
  
  #print("max(1-A,1-B):", max(1-A,1-B))
  #print("min(N-A,N-B):", min(N-A,N-B))
  #print("max(1-A,B-N):", max(1-A,B-N))
  #print("min(N-A,B-1):", min(N-A,B-1))
  
  #print("P+i-1:", P+i-1)
  #print("R+j-1:", R+j-1)
  
  for i in range(P, Q+1):
    for j in range(R, S+1):
      if (max(1-A,1-B) <= i <= min(N-A,N-B)) and (A+i, B+i) == (i, j):
        print("#", end="")
      elif (max(1-A,B-N) <= i <= min(N-A,B-1)) and (A+i, B-i) == (i, j):
        print("#", end="")
      else:
        print(".", end="")
    print()

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    for i in range(p, q + 1):
        for j in range(r, s + 1):
            if (i - a) == (j - b) or (i - a) == (b - j):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 7

def problems230_c():
    pass

=======
Suggestion 8

def main():
    n,a,b = map(int, input().split())
    p,q,r,s = map(int, input().split())
    for i in range(p,q+1):
        for j in range(r,s+1):
            if (i-a==j-b) or (i-a==b-j) or (a-i==j-b) or (a-i==b-j):
                print('#', end='')
            else:
                print('.', end='')
        print()

=======
Suggestion 9

def get_input():
    line1 = input().split()
    line2 = input().split()
    return line1, line2

=======
Suggestion 10

def printGrid(N, A, B, P, Q, R, S):
    # 1. 先把所有格子都填上.，再把需要涂黑的格子填上#
    grid = [['.' for col in range(S-R+1)] for row in range(Q-P+1)]
    # 2. 涂黑(A+k,B+k)和(A+k,B-k)两个点
    for k in range(max(1-A,1-B), min(N-A,N-B)+1):
        grid[A+k-P][B+k-R] = '#'
    for k in range(max(1-A,B-N), min(N-A,B-1)+1):
        grid[A+k-P][B-k-R] = '#'
    # 3. 输出
    for row in grid:
        print(''.join(row))
