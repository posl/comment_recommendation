def problem287_a():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if s.count('For') > s.count('Against'):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problem287_a()