def main():
    S = input()
    count = 0
    if len(S) % 2 == 0:
        for i in range(len(S)//2):
            if S[i] != S[len(S)-1-i]:
                count += 1
    else:
        for i in range(len(S)//2):
            if S[i] != S[len(S)-1-i]:
                count += 1
    print(count)
