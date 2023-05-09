def main():
    N = int(input())
    A = set()
    B = set()
    for i in range(N):
        A.add(int(input()))
        B.add(int(input()))
    for i in range(1, 2*N+2):
        if i not in A and i not in B:
            print(i)
            break
