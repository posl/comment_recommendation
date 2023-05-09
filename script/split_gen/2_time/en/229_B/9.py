def solve():
    A, B = [int(x) for x in input().split()]
    print('Hard' if str(A + B)[-1] == '0' else 'Easy')
