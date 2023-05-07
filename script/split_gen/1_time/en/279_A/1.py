def main():
    S = input()
    bottoms = 0
    for i in range(len(S)-1):
        if S[i] == 'v' and S[i+1] == 'v':
            bottoms += 1
    print(bottoms)
