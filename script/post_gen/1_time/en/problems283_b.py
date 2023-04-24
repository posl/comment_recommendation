Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        elif query[0] == 2:
            print(A[query[1]-1])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1] - 1] = query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        elif query[0] == 2:
            print(A[query[1]-1])
        else:
            pass

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            print(A[query[1]-1])

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    for i in range(Q):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            print(A[query[1]-1])

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    for i in range(Q):
        query = [int(x) for x in input().split()]
        if len(query) == 2:
            print(A[query[1] - 1])
        else:
            A[query[1] - 1] = query[2]

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            A[query[1] - 1] = query[2]
        else:
            print(A[query[1] - 1])

=======
Suggestion 8

def main():
    #Get the number of elements in the sequence
    n = int(input())
    #Get the sequence
    a = list(map(int, input().split()))
    #Get the number of queries
    q = int(input())
    #Process the queries
    for _ in range(q):
        #Get the query
        query = list(map(int, input().split()))
        #If the query is to set the value of an element in the sequence
        if query[0] == 1:
            #Get the index of the element to set
            k = query[1]
            #Get the value to set the element to
            x = query[2]
            #Set the value of the element
            a[k - 1] = x
        #If the query is to print the value of an element in the sequence
        else:
            #Get the index of the element to print
            k = query[1]
            #Print the value of the element
            print(a[k - 1])
