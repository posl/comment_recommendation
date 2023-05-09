def main():
    H,N = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if H<=A[-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()