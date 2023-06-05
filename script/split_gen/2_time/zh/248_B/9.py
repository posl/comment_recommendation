def main():
    S = input()
    S = [int(x) for x in S]
    S.sort()
    for i in range(1,10):
        if i not in S:
            print(i)
            break
