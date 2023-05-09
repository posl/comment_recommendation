def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print(max(min(B) - max(A) + 1, 0))

if __name__ == '__main__':
    main()