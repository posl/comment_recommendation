def main():
    A, B, C = map(int, input().split())
    if (A-B) >= C:
        print(0)
    else:
        print(C-(A-B))

if __name__ == '__main__':
    main()