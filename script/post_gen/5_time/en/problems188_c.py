Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #N = int(input())
    #A = list(map(int, input().split()))
    N = 4
    A = [6,13,12,5,3,7,10,11,16,9,8,15,2,1,14,4]
    #N = 2
    #A = [1,4,2,5]
    #N = 2
    #A = [3,1,5,4]
    #N = 3
    #A = [3,1,2,4,6,5,7,8]
    #N = 4
    #A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #N = 5
    #A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #N = 16
    #A = [i for i in range(1, 2**N + 1)]
    #N = 16
    #A = [i for i in range(2**N, 0, -1)]
    #N = 16
    #A = [i for i in range(1, 2**N + 1)]
    #N = 16
    #A = [i for i in range(2**N, 0, -1)]
    #N = 16
    #A = [i for i in range(1, 2**N + 1)]
    #N = 16
    #A = [i for i in range(2**N, 0, -1)]
    #N = 16
    #A = [i for i in range(1, 2**N + 1)]
    #N = 16
    #A = [i for i in range(2**N, 0, -1)]
    #N = 16
    #A = [i for i in range(1, 2**N + 1)]
    #N = 16
    #A = [i for i in range(2**N, 0, -1)]
    #N =

=======
Suggestion 2

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A, reverse=True)
    print(A.index(B[1])+1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(A[i], i+1) for i in range(2**N)]

    while len(A) > 2:
        B = []
        for i in range(0, len(A), 2):
            if A[i][0] > A[i+1][0]:
                B.append(A[i])
            else:
                B.append(A[i+1])
        A = B

    if A[0][0] > A[1][0]:
        print(A[1][1])
    else:
        print(A[0][1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
    A = A[:2**N]
    A = sorted(A, key=lambda x: x[0])
    print(A[1][0] + 1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = B[-1]
    D = B[-2]
    E = A.index(D)
    print(E+1)
main()

=======
Suggestion 7

def main():
    # input
    N = int(input())
    A = [int(x) for x in input().split()]

    # compute
    B = [[A[2*i], A[2*i+1]] for i in range(2**(N-1))]
    B.sort(key=lambda x:x[1])
    B.sort(key=lambda x:x[0])

    # output
    print(A.index(B[-2][1])+1)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [(i, a[i]) for i in range(len(a))]
    while True:
        if len(a) == 2:
            print(min(a[0], a[1], key=lambda x: x[1])[0] + 1)
            break
        a = [(i, max(a[j], a[j + 1], key=lambda x: x[1])) for i, j in enumerate(range(0, len(a), 2))]
        a = [a[i] for i in range(len(a)) if i % 2 == 0]
    return 0

=======
Suggestion 9

def get_first_place(players):
    if len(players) == 1:
        return players[0]
    else:
        new_players = []
        for i in range(0, len(players), 2):
            new_players.append(max(players[i], players[i+1]))
        return get_first_place(new_players)

=======
Suggestion 10

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    #print(N, A)
    B = sorted(A)
    #print(B)
    C = B[-2]
    #print(C)
    print(A.index(C)+1)

main()
