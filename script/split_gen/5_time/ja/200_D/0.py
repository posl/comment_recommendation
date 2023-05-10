def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(1,N+1):
        if i % 2 == 0:
            B.append(i)
        else:
            C.append(i)
    print("Yes")
    print(len(B), *B)
    print(len(C), *C)
