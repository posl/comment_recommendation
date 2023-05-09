def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print('Yes' if len(s) == n and all(s[i][0] in ['H', 'D', 'C', 'S'] for i in range(n)) and all(s[i][1] in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'] for i in range(n)) else 'No')

if __name__ == '__main__':
    main()