def main():
    n = int(input())
    if n < 42:
        print('AGC{:0=3}'.format(n))
    else:
        print('AGC{:0=3}'.format(n+1))
