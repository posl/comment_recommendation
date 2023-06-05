def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        for i in range(t, t + k):
            k %= 3
            if s[i] == 'a':
                if k == 0:
                    print('a')
                    break
                elif k == 1:
                    print('b')
                    break
                else:
                    print('c')
                    break
            elif s[i] == 'b':
                if k == 0:
                    print('b')
                    break
                elif k == 1:
                    print('c')
                    break
                else:
                    print('a')
                    break
            else:
                if k == 0:
                    print('c')
                    break
                elif k == 1:
                    print('a')
                    break
                else:
                    print('b')
                    break

if __name__ == '__main__':
    main()