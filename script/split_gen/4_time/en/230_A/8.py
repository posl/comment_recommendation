def main():
    n = int(input())
    if n <= 54:
        print('AGC{:03}'.format(n))
    else:
        print('AGC{:03}'.format(n + 1))
