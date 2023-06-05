def main():
    S = input()
    T = input()
    correct = 0
    for i in range(3):
        if S[i] == T[i]:
            correct += 1
    print(correct)
