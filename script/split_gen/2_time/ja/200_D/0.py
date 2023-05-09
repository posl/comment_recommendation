def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(N):
        if A[i] % 200 == 0:
            B.append(i+1)
        else:
            C.append(i+1)
    if len(B) >= 2:
        print("Yes")
        print(len(B), *B)
        print(1, B[0])
        return
    if len(C) >= 2:
        print("Yes")
        print(1, C[0])
        print(len(C), *C)
        return
    print("No")
