def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    A_min = min(A)
    B_min = min(B)
    if A.index(A_min) == B.index(B_min):
        A.pop(A.index(A_min))
        B.pop(B.index(B_min))
        A_min = min(A)
        B_min = min(B)
        print(min(A_min+B_min, max(A_min
