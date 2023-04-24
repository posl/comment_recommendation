Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.append(X)
    y.append(Y)
    if max(x) < min(y):
        print("No War")
    else:
        print("War")

=======
Suggestion 2

def main():
    N, M, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.append(X)
    B.append(Y)
    A.sort()
    B.sort()
    if A[-1] < B[0]:
        print('No War')
    else:
        print('War')

main()

=======
Suggestion 3

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and min(y) > X:
        print("No War")
    else:
        print("War")

=======
Suggestion 4

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x_max = max(x)
    y_min = min(y)

    if x_max < y_min and X < y_min <= Y:
        print('No War')
    else:
        print('War')

=======
Suggestion 5

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    if x[-1] < y[0] and X < y[0] and y[0] <= Y:
        print("No War")
    else:
        print("War")

=======
Suggestion 6

def main():
    N, M, X, Y = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and X < min(y):
        print('No War')
    else:
        print('War')

=======
Suggestion 7

def main():
    N, M, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #print(N, M, X, Y)
    #print(A)
    #print(B)
    
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    
    for i in range(X, Y+1):
        if A[-1] < i and i <= B[0]:
            print("No War")
            exit()
    print("War")

=======
Suggestion 8

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    X = max(x)
    Y = min(y)

    if(X < Y):
        print("No War")
    else:
        print("War")

=======
Suggestion 9

def main():
    #入力
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    #解答
    if max(x) < min(y) and max(x) < Y and min(y) > X:
        print('No War')
    else:
        print('War')
