Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print(min(n*a, b))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    print(min(A * N, B))

=======
Suggestion 3

def   main ( ) : 
     n ,   a ,   b   =   map ( int ,   input ( ) . split ( ) ) 
     print ( min ( a * n ,   b ) )

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    print(min(a*n, b))
main()

=======
Suggestion 5

def main():
    #input
    N, A, B = map(int, input().split())
    #output
    print(min(N*A, B))

=======
Suggestion 6

def main():
    # read input
    N, A, B = map(int, input().split())

    # compute
    train = N * A
    taxi = B

    # output
    print(min(train, taxi))

=======
Suggestion 7

def main():
    #Get the input
    N, A, B = map(int, input().split())
    #Calculate the minimum travel cost
    trainCost = N * A
    taxiCost = B
    minTravelCost = min(trainCost, taxiCost)
    #Print the minimum travel cost
    print(minTravelCost)
