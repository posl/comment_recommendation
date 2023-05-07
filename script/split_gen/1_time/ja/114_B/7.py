def main():
    S = input()
    S = S.replace(" ", "")
    S = S.replace("
", "")
    if len(S) < 4:
        print(753 - int(S))
    else:
        min = 753 - int(S[0:3])
        for i in range(len(S) - 2):
            if min > 753 - int(S[i:i+3]):
                min = 753 - int(S[i:i+3])
        print(min)
