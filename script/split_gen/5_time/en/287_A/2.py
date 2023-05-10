def main():
    n = int(input())
    s = [input() for i in range(n)]
    print('Yes' if s.count('For') > s.count('Against') else 'No')
