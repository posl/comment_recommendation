def main():
    r,c = input().split()
    r = int(r)
    c = int(c)
    A = []
    for i in range(2):
        A.append(input().split())
        A[i][0] = int(A[i][0])
        A[i][1] = int(A[i][1])
    print(A[r-1][c-1])
