def main():
    a = input().split()
    a = list(map(int, a))
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')
