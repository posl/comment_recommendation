def main():
    S = input()
    odd = S[0::2]
    even = S[1::2]
    if odd.find('L') == -1 and odd.find('R') == -1 and even.find('U') == -1 and even.find('D') == -1:
        print('Yes')
    else:
        print('No')
