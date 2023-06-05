def main():
    S = input()
    S = list(S)
    S.sort()
    count = 1
    for i in range(2):
        if S[i] != S[i+1]:
            count += 1
    print(count)
