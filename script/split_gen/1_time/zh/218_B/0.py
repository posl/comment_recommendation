def main():
    p = input().strip().split()
    p = [int(i) for i in p]
    p = [chr(96 + i) for i in p]
    print(''.join(p))
