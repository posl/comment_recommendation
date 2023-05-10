def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == 'L':
                print("No")
                return
        else:
            if S[i] == 'R':
                print("No")
                return
    print("Yes")
