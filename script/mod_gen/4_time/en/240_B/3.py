def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    print(len(set(a_list)))

if __name__ == '__main__':
    main()