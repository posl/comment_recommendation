def main():
    # input
    n = int(input())
    s = [input() for i in range(n)]
    # compute
    # output
    if s.count('For') > s.count('Against'):
        print('Yes')
    else:
        print('No')
