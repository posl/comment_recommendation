def main():
    N = input()
    if N == '0':
        print('Yes')
        return
    if int(N) % 9 == 0:
        print('Yes')
    else:
        print('No')
