def main():
    S = input()
    S = list(S)
    S = [int(i) for i in S]
    S.sort()
    for i in range(1,10):
        if i not in S:
            print(i)
            break
