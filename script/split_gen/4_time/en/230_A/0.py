def main():
    N = int(input())
    if N < 43:
        print('AGC' + str(N).zfill(3))
    else:
        print('AGC' + str(N + 1).zfill(3))
