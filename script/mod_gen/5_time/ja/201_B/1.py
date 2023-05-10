def main():
    n = int(input())
    mountains = []
    for _ in range(n):
        name, height = input().split()
        mountains.append([name, int(height)])
    mountains.sort(key=lambda x: -x[1])
    print(mountains[1][0])

if __name__ == '__main__':
    main()