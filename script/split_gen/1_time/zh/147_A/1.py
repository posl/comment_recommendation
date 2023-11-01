def main():
    a = input().split()
    a = [int(i) for i in a]
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')
