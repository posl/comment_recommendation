def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(T)):
        if S[i] != T[i]:
            count += 1
    print(count)
