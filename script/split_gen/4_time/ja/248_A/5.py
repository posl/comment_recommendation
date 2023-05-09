def main():
    S = input()
    S = list(map(int, S))
    S.sort()
    for i in range(1, 10):
        if i != S[i-1]:
            print(i)
            break
