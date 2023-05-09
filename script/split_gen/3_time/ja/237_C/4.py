def main():
    S = input()
    N = len(S)
    if S == S[::-1]:
        print("Yes")
        return
    for i in range(N):
        if S[:i+1] == S[:i+1][::-1]:
            print("Yes")
            return
    print("No")
