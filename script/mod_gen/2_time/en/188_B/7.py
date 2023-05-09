def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()