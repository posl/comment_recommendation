def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountains.append(input().split())
    mountains = sorted(mountains, key=lambda mountain: mountain[1], reverse=True)
    print(mountains[1][0])

if __name__ == '__main__':
    main()