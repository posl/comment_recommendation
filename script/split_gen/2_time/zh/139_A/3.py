def main():
    S = input()
    T = input()
    result = 0
    for i in range(3):
        if S[i] == T[i]:
            result += 1
    print(result)
