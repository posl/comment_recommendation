def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if s < a:
            print('No')
        elif a == s:
            print('Yes')
        else:
            if s % 2 != a % 2:
                print('No')
            else:
                if s % 2 == 0:
                    print('Yes')
                else:
                    print('No')
