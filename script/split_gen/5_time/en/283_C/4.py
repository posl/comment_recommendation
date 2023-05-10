def main():
    S = input()
    keystrokes = 0
    for i in range(len(S)):
        if S[i] == "0":
            keystrokes += 1
        else:
            keystrokes += 2
    print(keystrokes-1)
