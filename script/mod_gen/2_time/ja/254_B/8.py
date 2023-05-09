def main():
    N = int(input())
    for i in range(N):
        tmp = [1]
        for j in range(i):
            tmp.append(tmp[j] + tmp[j-1])
        print(*tmp)

if __name__ == '__main__':
    main()