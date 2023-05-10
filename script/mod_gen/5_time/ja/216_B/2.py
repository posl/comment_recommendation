def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input())
    if len(set(name)) != len(name):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()