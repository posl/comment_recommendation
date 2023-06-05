def main():
    str = input()
    odd = str[0::2]
    even = str[1::2]
    if odd.islower() and even.isupper():
        print('Yes')
    else:
        print('No')
