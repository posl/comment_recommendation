def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    C = [B[x-1] for x in C]
    print(sum(A.count(x) for x in C))

if __name__ == '__main__':
    main()