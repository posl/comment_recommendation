def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                print(0, end='')
            else:
                print(1, end='')
        print('')
