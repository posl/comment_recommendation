def main():
    n = int(input())
    s = input()
    for i in s:
        if ord(i)+n > ord('Z'):
            print(chr(ord(i)+n-26),end='')
        else:
            print(chr(ord(i)+n),end='')
    print()
