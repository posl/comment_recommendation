def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [1/a for a in A]
    print(1/sum(B))

if __name__ == '__main__':
    main()