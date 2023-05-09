def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    count = 1
    i = 0
    j = 0
    while(i < h-1 or j < w-1):
        if i < h-1 and c[i+1][j] == ".":
            count += 1
            i += 1
        elif j < w-1 and c[i][j+1] == ".":
            count += 1
            j += 1
        else:
            break
    print(count)

if __name__ == '__main__':
    main()