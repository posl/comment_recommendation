def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = [b-1 for b in B]
    A.sort(reverse=True)
    for i in range(K):
        if A[i] in B:
            print("Yes")
            return
    print("No")
main()
