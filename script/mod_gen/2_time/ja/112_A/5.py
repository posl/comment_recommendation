def main():
    N = int(input())
    if N == 1:
        print("Hello World")
    else:
        A, B = map(int, input().split())
        print(A + B)

if __name__ == '__main__':
    main()