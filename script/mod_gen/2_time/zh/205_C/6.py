def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    if(A == list(range(1,N+1))):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()