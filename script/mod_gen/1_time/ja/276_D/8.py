def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%2 if a%2 == 1 else a%3 if a%3 == 1 else a for a in A]
    if len(set(A)) == 1 and A[0] == 1:
        print(0)
    else:
        print(-1)

if __name__ == '__main__':
    main()