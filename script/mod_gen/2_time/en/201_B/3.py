def main():
    N = int(input())
    mountain_list = []
    for i in range(N):
        mountain_list.append(input().split())
    mountain_list.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain_list[1][0])

if __name__ == '__main__':
    main()