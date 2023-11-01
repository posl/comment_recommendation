def main():
    n = int(input())
    s = input()
    if '1' in s[::2]:
        print('Takahashi')
    else:
        print('Aoki')
