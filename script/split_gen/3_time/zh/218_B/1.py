def main():
    P = input().split()
    S = [chr(int(P[i])+96) for i in range(26)]
    print(''.join(S))
