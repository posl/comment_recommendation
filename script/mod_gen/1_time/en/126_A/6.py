def lowerCaseKthCharacter(N, K, S):
    if K > N:
        return "K should be less than N"
    else:
        return S[:K-1] + S[K-1].lower() + S[K:]

if __name__ == '__main__':
    lowerCaseKthCharacter()