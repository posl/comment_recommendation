def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if M > N:
        print("No")
        return
    for b in B:
        if b > A[-1]:
            print("No")
            return
        for i in range(len(A)):
            if A[i] >= b:
                A.pop(i)
                break
    print("Yes")
