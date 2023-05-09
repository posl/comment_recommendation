def main():
    A, B = map(int, input().split())
    if A + B > 16:
        print(':(')
    else:
        print('Yay!')
