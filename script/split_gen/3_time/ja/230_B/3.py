def main():
    S = input()
    T = "oxx" * 10**5
    for i in range(len(T) - len(S) + 1):
        if T[i:i+len(S)] == S:
            print("Yes")
            return
    print("No")
