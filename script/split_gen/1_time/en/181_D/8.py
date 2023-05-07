def main():
    S = input()
    if "8" in S:
        print("Yes")
        return
    for i in range(len(S)):
        for j in range(len(S)):
            if i == j:
                continue
            if int(S[i]+S[j])%8 == 0:
                print("Yes")
                return
    print("No")
