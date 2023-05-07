def main():
    S = input()
    T = input()
    diff = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diff += 1
    print(diff)
