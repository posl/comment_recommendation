def main():
    n = int(input())
    if n >= 42:
        print('AGC' + str(n + 1).rjust(3, '0'))
    else:
        print('AGC' + str(n).rjust(3, '0'))
