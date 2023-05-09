def main():
    S = input()
    i = 0
    j = len(S) - 1
    count = 0
    while i < j:
        if S[i] != S[j]:
            count += 1
        i += 1
        j -= 1
    print(count)
