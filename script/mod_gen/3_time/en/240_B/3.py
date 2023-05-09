def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(len(set(A)))

if __name__ == '__main__':
    main()