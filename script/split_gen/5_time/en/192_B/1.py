def main():
    s = input()
    odd = s[0::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        print('Yes')
    else:
        print('No')
