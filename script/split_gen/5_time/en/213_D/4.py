def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A,B)
    visited = [1]
    for i in range(N-1):
        if A[i] == 1 or B[i] == 1:
            if A[i] in visited:
                visited.append(B[i])
            else:
                visited.append(A[i])
    print(*visited)
