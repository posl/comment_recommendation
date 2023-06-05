def main():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        mountains.append((s, int(t)))
    mountains.sort(key=lambda x: x[1])
    print(mountains[-2][0])

if __name__ == '__main__':
    main()