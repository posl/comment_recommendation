def main():
    S = input()
    count = 0
    while S != "0":
        if S[-1] == "0":
            S = S[:-1]
        else:
            S = str(int(S) - 1)
        count += 1
    print(count)
