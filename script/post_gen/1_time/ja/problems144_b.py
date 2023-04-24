Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if N == i * j:
                print('Yes')
                return
    print('No')

=======
Suggestion 3

def main():
    N = int(input())
    flag = False
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                flag = True
                break
        if flag:
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i * j == N:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n // i < 10:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 6

def main():
    N = int(input())
    for i in range(1,10):
        if N % i == 0 and 1 <= N / i <= 9:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    n = int(input())
    if n == 1:
        print('No')
        return
    for i in range(1, 10):
        if n % i == 0 and n // i < 10:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
  N = int(input())
  for i in range(1, 10):
    if N % i == 0 and N // i < 10:
      print('Yes')
      return
  print('No')

main()

=======
Suggestion 9

def main():
    n = int(input())
    if n < 10:
        print("Yes")
    else:
        for i in range(1, 10):
            if n % i == 0 and n // i < 10:
                print("Yes")
                return
        print("No")

=======
Suggestion 10

def main():
  N = int(input())
  for i in range(1,10):
    if N%i == 0:
      if N//i <= 9:
        print("Yes")
        return
  print("No")
  return
