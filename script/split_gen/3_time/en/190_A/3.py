def main():
    a, b, c = map(int, input().split())
    if (a > b and c == 0) or (a < b and c == 1):
        print('Takahashi')
    else:
        print('Aoki')
