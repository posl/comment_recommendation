def solve():
    #coding:utf-8
    n = input()
    if n == '0':
        print('Yes')
        return
    if len(n) == 1:
        print('No')
        return
    num = 0
    for i in n:
        num += int(i)
    if num % 9 == 0:
        print('Yes')
    else:
        print('No')
    return

if __name__ == '__main__':
    solve()