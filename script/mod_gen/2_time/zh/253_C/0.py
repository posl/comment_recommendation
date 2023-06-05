def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    print(s)
    print(h, w)

if __name__ == '__main__':
    main()