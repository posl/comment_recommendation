def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[:m]))

if __name__ == '__main__':
    main()