def main():
    A, B, C = map(int, input().split())
    print(max(A + B, B + C, A + C))

if __name__ == '__main__':
    main()