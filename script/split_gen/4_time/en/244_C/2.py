def main():
    N = int(input())
    A = set()
    B = set()
    for i in range(1, 2*N+2):
        A.add(i)
    for i in range(1, 2*N+2):
        B.add(i)
    for i in range(N):
        print(i+1)
        a = int(input())
        A.remove(a)
        B.remove(a)
        print(2*N+2-i)
        b = int(input())
        A.remove(b)
        B.remove(b)
    print(A.pop())
    input()
