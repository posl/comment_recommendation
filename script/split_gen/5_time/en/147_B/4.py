def main():
    S = input()
    count = 0
    for i in range(0, int(len(S)/2)):
        if S[i] != S[-1-i]:
            count += 1
    print(count)
