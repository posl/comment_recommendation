def main():
    N = int(input())
    S = [input() for i in range(N)]
    for s in S:
        if s == 'Against':
            print('No')
            return
    print('Yes')
    return
