def last_card(N,K,A):
    if N <= K:
        return 1
    else:
        if (N % K) == 0:
            return 0
        else:
            return 1

if __name__ == '__main__':
    last_card()