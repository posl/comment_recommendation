def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(200):
        if x - i not in p:
            print(x - i)
            break
        elif x + i not in p:
            print(x + i)
            break

if __name__ == '__main__':
    main()