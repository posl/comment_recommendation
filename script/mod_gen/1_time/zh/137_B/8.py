def main():
    k, x = map(int, input().split())
    list = []
    for i in range(x-k+1,x+k):
        list.append(i)
    print(*list)

if __name__ == '__main__':
    main()