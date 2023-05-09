def main():
    n = int(input())
    a = 0
    b = 0
    for i in range(n):
        s = input()
        if s == 'For':
            a += 1
        elif s == 'Against':
            b += 1
    if a > b:
        print('Yes')
    else:
        print('No')
