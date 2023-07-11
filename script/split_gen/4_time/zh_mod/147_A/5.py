def main():
    A = input().split()
    A = list(map(int, A))
    if sum(A) >= 22:
        print('bust')
    else:
        print('win')
