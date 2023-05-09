def main():
    A, B, X = map(int, input().split())
    N = 0
    for i in range(10, 0, -1):
        if A * i + B * len(str(i)) <= X:
            N = i
            break
    print(N)

if __name__ == '__main__':
    main()