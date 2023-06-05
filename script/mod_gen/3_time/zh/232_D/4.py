def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    print(walk(h, w, c))

if __name__ == '__main__':
    main()