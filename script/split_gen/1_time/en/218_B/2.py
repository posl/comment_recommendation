def main():
    P = [int(i) for i in input().split()]
    S = [chr(i+96) for i in P]
    print(''.join(S))
