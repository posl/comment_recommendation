def main():
    S = input()
    lenS = len(S)
    count = 0
    for i in range(lenS // 2):
        if S[i] != S[lenS - 1 - i]:
            count += 1
    print(count)
