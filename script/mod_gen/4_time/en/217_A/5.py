def lexicographical_order():
    S, T = input().split()
    if S < T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    lexicographical_order()