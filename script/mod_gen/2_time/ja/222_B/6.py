def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([x for x in a if x < P]))

if __name__ == '__main__':
    main()