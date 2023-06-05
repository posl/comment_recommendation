def main():
    n = int(input())
    works = [list(map(int, input().split())) for i in range(n)]
    works.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += works[i][0]
        if time > works[i][1]:
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    main()