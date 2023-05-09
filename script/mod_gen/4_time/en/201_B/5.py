def main():
    n = int(input())
    mountains = {}
    for i in range(n):
        s, t = input().split()
        mountains[s] = int(t)
    print(sorted(mountains, key=mountains.get)[-2])

if __name__ == '__main__':
    main()