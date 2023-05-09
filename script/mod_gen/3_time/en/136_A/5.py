def main():
    A, B, C = map(int, input().split(' '))
    if C - (A - B) > 0:
        print(C - (A - B))
    else:
        print(0)

if __name__ == '__main__':
    main()