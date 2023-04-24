Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i+1] += 1
        if H[i] > H[i+1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i] < h[i + 1]:
            h[i + 1] -= 1
        if h[i] > h[i + 1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] - H[i+1] == 1:
            H[i+1] += 1
        elif H[i] - H[i+1] > 1:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] - H[i+1] > 1:
            print('No')
            return
        elif H[i] - H[i+1] == 1:
            H[i+1] += 1
    print('Yes')

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i - 1] < H[i]:
            H[i] -= 1
        if H[i - 1] > H[i]:
            print("No")
            return
    print("Yes")

main()

=======
Suggestion 6

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            H[i + 1] += 1
        if H[i] > H[i + 1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
  n = int(input())
  h = list(map(int, input().split()))
  for i in range(n-1):
    if h[i] > h[i+1]:
      h[i+1] += 1
    if h[i] > h[i+1]:
      print('No')
      return
  print('Yes')

=======
Suggestion 8

def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    H.append(0)
    for i in range(N):
        if H[i] - H[i+1] > 1:
            print("No")
            break
        elif H[i] - H[i+1] == 1:
            H[i+1] += 1
    else:
        print("Yes")

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i] < H[i-1]:
            if H[i] + 1 != H[i-1]:
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h = [0] + h
    for i in range(1, n + 1):
        if h[i] - h[i - 1] > 1:
            print("No")
            exit()
        if h[i] - h[i - 1] == 1:
            h[i] -= 1
    print("Yes")
