def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print('Yes' if s.count('For') > s.count('Against') else 'No')

if __name__ == '__main__':
    main()