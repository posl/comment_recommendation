Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b + 1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B + 1):
        if i % C == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 4

def main():
  A, B, C = map(int, input().split())
  ans = -1
  for i in range(A, B+1):
    if i % C == 0:
      ans = i
      break
  print(ans)

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    if A % C == 0:
        print(A)
    elif B % C == 0:
        print(B)
    elif A < C and B < C:
        print(-1)
    else:
        print(C * (B // C))

=======
Suggestion 6

def main():
    input = raw_input().split()
    A = int(input[0])
    B = int(input[1])
    C = int(input[2])
    
    for i in range(A, B+1):
        if i%C == 0:
            print i
            return
    print -1

=======
Suggestion 7

def main():
    #Get input
    A, B, C = map(int, input().split())
    
    #Check for multiples
    for i in range(A, B+1):
        if i%C == 0:
            print(i)
            return
    #If no multiples
    print(-1)

=======
Suggestion 8

def main():
    # Get the input
    A, B, C = map(int, input().split())

    # Check if there is a number between A and B (inclusive) that is a multiple of C
    if A % C == 0:
        print(A)
    elif B % C == 0:
        print(B)
    else:
        # Find the first number between A and B (inclusive) that is a multiple of C
        for i in range(A+1, B+1):
            if i % C == 0:
                print(i)
                break
        else:
            print(-1)
