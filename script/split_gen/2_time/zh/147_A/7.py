def main():
    a = input()
    a = a.split(' ')
    a = list(map(int, a))
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')
