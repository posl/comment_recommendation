def main():
    import sys
    N = int(input())
    A = []
    B = []
    for i in range(N):
        q = sys.stdin.readline().split()
        if q[0] == '1':
            A.append(int(q[1]))
            B.append(int(q[2]))
        else:
            print(sum(A[:int(q[1])]) * sum(B[:int(q[1])]))
            A = A[int(q[1]):]
            B = B[int(q[1]):]
