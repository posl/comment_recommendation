def main():
    A = list(map(int, input().split()))
    if sum(A) > 21:
        print('bust')
    else:
        print('win')
