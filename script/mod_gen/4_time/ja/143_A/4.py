def main():
    A, B = map(int, input().split())
    print(max(0, A - 2*B))

if __name__ == '__main__':
    main()