def main():
    A, B, T = map(int, input().split())
    print(int(T // A * B))
    return

if __name__ == '__main__':
    main()