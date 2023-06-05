def main():
    N = int(input())
    print('Yay!' if int(N * 1.08) < 206 else 'so-so' if int(N * 1.08) == 206 else ':(')
