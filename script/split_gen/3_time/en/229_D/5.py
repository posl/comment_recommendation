def main():
    S, K = input().split()
    K = int(K)
    S = S.replace('.', 'X')
    print(max([len(x) for x in S.split('X')]) + min(K, S.count('.')))
