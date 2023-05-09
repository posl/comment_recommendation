def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    if len(names) != len(set([tuple(i) for i in names])):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()