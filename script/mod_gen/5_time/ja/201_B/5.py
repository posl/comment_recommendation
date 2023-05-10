def main():
    # input
    n = int(input())
    mountains = []
    for _ in range(n):
        mountains.append(list(input().split()))
    # compute
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    # output
    print(mountains[1][0])

if __name__ == '__main__':
    main()