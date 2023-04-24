Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    print(min(N * A, B))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    print(min(A * N, B))

=======
Suggestion 3

def main():
  n,a,b = map(int,input().split())
  if a*n < b:
    print(a*n)
  else:
    print(b)

=======
Suggestion 4

def main():
    # Input
    N, A, B = map(int, input().split())
    # Output
    print(min(N*A, B))

=======
Suggestion 5

def main():
    # Get the input
    N, A, B = map(int, input().split())
    # Calculate the minimum total travel expense
    min_expense = min(N * A, B)
    # Print the minimum total travel expense
    print(min_expense)

=======
Suggestion 6

def main():
    #read input
    line = input()
    num = line.split(" ")
    n = int(num[0])
    a = int(num[1])
    b = int(num[2])
    #calculate
    train = a*n
    taxi = b
    if train > taxi:
        print(taxi)
    else:
        print(train)
