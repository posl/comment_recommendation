def main():
    S = input()
    N = len(S)
    for i in range(N):
        if i % 2 == 0:
            if S[i] == "L":
                print("No")
                return
        else:
            if S[i] == "R":
                print("No")
                return
    print("Yes")
    return
