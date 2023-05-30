def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[0:int(N/2)] == S[int(N/2):]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
main()
