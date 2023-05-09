def main():
    N = input()
    while len(N) > 1:
        N = str(sum(map(int, N)))
    if N == '9':
        print('Yes')
    else:
        print('No')
