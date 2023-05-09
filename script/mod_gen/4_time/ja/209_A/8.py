def main():
    # n = int(input())
    # s = input()
    # n, k = map(int, input().split())
    a, b = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    # a = int(input())
    if b < a:
        print(0)
    else:
        print(b-a+1)

if __name__ == '__main__':
    main()