def main():
    p = [int(x) for x in input().split()]
    print(''.join([chr(ord('a') + x - 1) for x in p]))
