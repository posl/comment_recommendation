def main():
    L = int(input())
    path = []
    for i in range(L):
        path.append([i + 1, i + 2, 0])
        path.append([i + 1, i + 2, i + 1])
    path.append([L + 1, L + 2, 0])
    print(L + 2, len(path))
    for p in path:
        print(*p)

if __name__ == '__main__':
    main()