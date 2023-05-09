def main():
    S = input()
    K = int(input())
    X = S.replace('.', 'X')
    X = X.replace('X'*K, 'X')
    print(len(X))
