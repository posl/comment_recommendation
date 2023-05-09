def main():
    A, B = [int(x) for x in input().split()]
    print(max(A + A - 1, B + B - 1, A + B))

if __name__ == '__main__':
    main()