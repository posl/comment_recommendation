def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(" ".join(map(str,sorted(A,key = lambda x: -x))))

if __name__ == '__main__':
    main()