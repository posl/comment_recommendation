def main():
    S = input()
    odd = S[::2]
    even = S[1::2]
    if odd == odd.upper() and even == even.lower():
        print('Yes')
    else:
        print('No')
