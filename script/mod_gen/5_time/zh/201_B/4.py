def main():
    N = int(input())
    mountains = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        mountains.append((S, T))
    mountains.sort(key=lambda x: -x[1])
    print(mountains[1][0])

if __name__ == '__main__':
    main()