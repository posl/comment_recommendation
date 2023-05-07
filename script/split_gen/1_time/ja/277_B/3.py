def main():
    n = int(input())
    s = [input() for _ in range(n)]
    if len(set(s)) != n:
        print('No')
        return
    for si in s:
        if si[0] not in 'HDCK' or si[1] not in 'A23456789TJQK':
            print('No')
            return
    print('Yes')
