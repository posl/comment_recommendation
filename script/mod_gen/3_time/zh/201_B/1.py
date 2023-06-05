def main():
    N = int(input())
    mountains = []
    for i in range(N):
        S, T = input().split()
        mountains.append((S, int(T)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

if __name__ == '__main__':
    main()