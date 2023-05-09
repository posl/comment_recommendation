def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    a = set(a)
    b = set(b)
    if len(a) == 1 or len(b) == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()