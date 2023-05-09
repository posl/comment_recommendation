def main():
    S = input()
    K = int(input())
    S = S.replace('.', 'X')
    S = S.replace('X', 'X.')
    S = S.split('.')
    S.sort(key=len, reverse=True)
    print(S[0].count('X'))
