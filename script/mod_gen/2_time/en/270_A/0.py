def main():
    A, B = map(int, input().split())
    print(A + B - max(A, B))

if __name__ == '__main__':
    main()