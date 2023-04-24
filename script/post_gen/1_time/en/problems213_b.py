Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    print(A[1])

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    print(A.index(B[1])+1)

=======
Suggestion 5

def   main ():
    N  =  int ( input ())
    A  =  list ( map ( int ,  input (). split ()))
    A_min  =  min (A)
    A_max  =  max (A)
    A_min_index  =  A . index (A_min)
    A_max_index  =  A . index (A_max)
    if  A_min_index  <  A_max_index :
         print (A_max_index  +   1 )
    else :
         print (A_max_index  +   1 )
