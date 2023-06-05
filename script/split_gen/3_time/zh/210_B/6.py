def main():
    N = int(input())
    S = input()
    if '1' in S[::2]:
        print('高桥')
    else:
        print('青木')
