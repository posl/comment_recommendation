def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t,k = map(int, input().split())
        for i in range(t+1):
            s = s.replace('a', 'bc')
            s = s.replace('b', 'ca')
            s = s.replace('c', 'ab')
        print(s[k-1])

if __name__ == '__main__':
    main()