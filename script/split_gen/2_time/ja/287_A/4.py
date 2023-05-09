def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print('Yes' if s.count('For') > n/2 else 'No')
