def main():
    # input
    S = input()
    # process
    count = 0
    for i in range(len(S)//2):
        if S[i] != S[len(S)-1-i]:
            count += 1
    # output
    print(count)
