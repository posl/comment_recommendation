def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                pass
            else:
                print("DENIED")
                exit()
    print("APPROVED")

if __name__ == '__main__':
    main()