def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        elif a == s:
            print('Yes')
        else:
            if a % 2 == s % 2:
                print('Yes')
            else:
                print('No')
main()
