def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    S = {1: S1, 2: S2, 3: S3}
    print(''.join([S[int(t)] for t in T]))
