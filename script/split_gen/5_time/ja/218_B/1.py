def main():
    P = [int(x) for x in input().split()]
    S = [chr(ord('a') + (p - 1)) for p in P]
    print("".join(S))
