def main():
    n = int(input())
    if n < 42:
        print('AGC{:03}'.format(n))
    else:
        print('AGC{:02}'.format(n + 1))
