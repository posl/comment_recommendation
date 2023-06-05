def main():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        mountains.append((s, int(t)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

if __name__ == '__main__':
    main()