def sum_two_cards():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, c+a))

if __name__ == '__main__':
    sum_two_cards()