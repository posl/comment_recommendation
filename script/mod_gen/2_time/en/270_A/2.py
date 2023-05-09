def main():
    A, B = map(int, input().split())
    print(A + B - min(A, B))

if __name__ == '__main__':
    main()