def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    print('Yes' if len(set(name)) != len(name) else 'No')

if __name__ == '__main__':
    main()