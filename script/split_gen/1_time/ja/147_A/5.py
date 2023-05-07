def main():
    a = input().split()
    a = list(map(int, a))
    if sum(a) <= 21:
        print('win')
    else:
        print('bust')
