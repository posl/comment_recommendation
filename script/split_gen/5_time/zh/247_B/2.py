def get_result():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    print('Yes' if len(names) == len(set([name[0] for name in names] + [name[1] for name in names])) else 'No')
