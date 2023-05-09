def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    for i in range(2000):
        if i not in a_set:
            print(i)
            break

if __name__ == '__main__':
    main()