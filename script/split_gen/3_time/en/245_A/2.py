def main():
    a, b, c, d = map(int, input().split())
    if (a*60+b) < (c*60+d+1):
        print('Takahashi')
    else:
        print('Aoki')
