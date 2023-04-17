Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(abs(a[0] - a[1]) + abs(a[1] - a[2]))

=======

def main():
    A = [int(i) for i in input().split()]
    print(min(abs(A[0]-A[1])+abs(A[1]-A[2]),abs(A[0]-A[2])+abs(A[1]-A[2]),abs(A[0]-A[1])+abs(A[0]-A[2])))

main()

=======

def main():
    A = map(int, raw_input().split())
    A.sort()
    print A[1] - A[0] + A[2] - A[1]

=======

def main():
    A = list(map(int, input().split()))
    print(min([abs(A[0] - A[1]) + abs(A[1] - A[2]), abs(A[1] - A[0]) + abs(A[0] - A[2]), abs(A[2] - A[0]) + abs(A[0] - A[1])]))

=======

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

=======

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(abs(A[0] - A[2]))

=======

def main():
    A = [int(i) for i in input().split()]
    A.sort()
    print(A[2] - A[0])

=======

def main():
    A = list(map(int,input().split()))
    A.sort()
    print(A[1]-A[0])

=======

def main():
    a = [int(x) for x in input().split()]
    a = sorted(a)
    print(abs(a[2] - a[0]))
