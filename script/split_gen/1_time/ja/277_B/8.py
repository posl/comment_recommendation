def main():
    N = int(input())
    card = [input() for _ in range(N)]
    if len(set(card)) == N and all([c[0] in 'HDCS' and c[1] in 'A23456789TJQK' for c in card]):
        print('Yes')
    else:
        print('No')
