def main():
    S = input()
    for i in range(len(S)):
        if (i % 2 == 0 and S[i] == "L") or (i % 2 == 1 and S[i] == "R"):
            print("No")
            return
    print("Yes")
