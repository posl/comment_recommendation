Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        elif H[i] > H[i+1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i + 1] += 1
        if h[i] > h[i + 1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N - 1):
        if H[i] - H[i + 1] > 1:
            print("No")
            return
        elif H[i] - H[i + 1] == 1:
            H[i + 1] += 1
    print("Yes")

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] <= H[i+1]:
            continue
        elif H[i] == H[i+1] + 1:
            H[i] -= 1
        else:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i] < H[i-1]:
            H[i] += 1
        if H[i] < H[i-1]:
            return 'No'
    return 'Yes'

print(solve())

=======
Suggestion 8

def main():
  N = int(input())
  H = list(map(int,input().split()))
  if N == 1:
    print('Yes')
  else:
    for i in range(N-1):
      if H[i] > H[i+1]:
        H[i+1] += 1
    if H == sorted(H):
      print('Yes')
    else:
      print('No')
