def main():
    N = int(input())
    names = []
    for _ in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(i+1, N):
            if names[i] == names[j]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()