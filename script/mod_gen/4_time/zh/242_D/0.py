def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        for j in range(t):
            s = s.replace('a', 'bc').replace('b', 'ca').replace('c', 'ab')
        print(s[k-1])

if __name__ == '__main__':
    main()