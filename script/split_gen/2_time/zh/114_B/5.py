def main():
    S = input()
    l = len(S)
    diff = 1000
    for i in range(l-2):
        X = int(S[i:i+3])
        if abs(X-753) < diff:
            diff = abs(X-753)
    print(diff)
