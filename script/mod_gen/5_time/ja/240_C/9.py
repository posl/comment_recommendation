def main():
    N, X = map(int, input().split())
    result = "No"
    for i in range(N):
        a, b = map(int, input().split())
        if a <= X and X <= b:
            result = "Yes"
            break
    print(result)

if __name__ == '__main__':
    main()