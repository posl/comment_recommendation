def main():
    S = input()
    K = int(input())
    S = S.replace('.', '')
    S = S.replace('X', ' ')
    S = S.split(' ')
    S = list(map(len, S))
    S = list(map(lambda x: x - 1, S))
    S = list(filter(lambda x: x > 0, S))
    S = list(map(lambda x: x - 1, S))
    S = list(filter(lambda x: x > 0, S))
    S = list(map(lambda x: x // 2, S))
    S = list(map(lambda x: x * 2, S))
    S = sum(S)
    if K > 0:
        S += 1
    print(S)
