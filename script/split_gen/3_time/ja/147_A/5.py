def main():
    a = list(map(int, input().split()))
    s = sum(a)
    if s >= 22:
        print('bust')
    else:
        print('win')
