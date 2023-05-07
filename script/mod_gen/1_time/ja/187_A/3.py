def main():
    a, b = map(int, input().split())
    if sum(map(int, list(str(a)))) > sum(map(int, list(str(b)))): print(sum(map(int, list(str(a)))))
    else: print(sum(map(int, list(str(b)))))

if __name__ == '__main__':
    main()