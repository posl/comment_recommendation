def main():
    S = input()
    S = S.replace('?', '9')
    S = S.replace('x', '0')
    S = S.replace('o', '1')
    S = int(S, 2)
    ans = 0
    for i in range(10000):
        if i & S == i:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()