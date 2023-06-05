def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            tmp = list(S)
            tmp[i], tmp[j] = tmp[j], tmp[i]
            if "".join(tmp) == T:
                print("Yes")
                return
    print("No")
