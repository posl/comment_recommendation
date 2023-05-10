def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains = sorted(mountains, key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

if __name__ == '__main__':
    main()