def main():
    n = int(input())
    bridges = list(map(int, input().split()))
    max_height = 0
    for height in bridges:
        if height > max_height:
            max_height = height
    for i in range(n):
        if bridges[i] == max_height:
            print(i+1)
            break

if __name__ == '__main__':
    main()