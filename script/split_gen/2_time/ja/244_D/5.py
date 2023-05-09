def main():
    S = list(input().split())
    T = list(input().split())
    if S == T:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['R', 'B', 'G']:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['G', 'R', 'B']:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['G', 'B', 'R']:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['B', 'R', 'G']:
        print('Yes')
    elif S == ['R', 'G', 'B'] and T == ['B', 'G', 'R']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['R', 'G', 'B']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['G', 'R', 'B']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['G', 'B', 'R']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['B', 'R', 'G']:
        print('Yes')
    elif S == ['R', 'B', 'G'] and T == ['B', 'G', 'R']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['R', 'G', 'B']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['R', 'B', 'G']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['G', 'B', 'R']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['B', 'R', 'G']:
        print('Yes')
    elif S == ['G', 'R', 'B'] and T == ['B', 'G', 'R']:
        print('Yes')
    elif S == ['G', 'B', 'R'] and T == ['R', 'G
