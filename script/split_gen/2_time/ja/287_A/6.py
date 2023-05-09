def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s.count('For') > s.count('Against'):
            print('Yes')
            break
        else:
            print('No')
            break
