def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
    else:
        for i in range(N):
            if A[i] != i:
                print(i)
                break
        else:
            print(N)
main()
