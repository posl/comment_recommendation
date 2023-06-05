def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a = max(a_list)
    b = min(b_list)
    if b - a < 0:
        print(0)
    else:
        print(b - a + 1)

if __name__ == '__main__':
    main()