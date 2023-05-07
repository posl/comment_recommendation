def main():
    S = input()
    if "0" in S:
        print("Yes")
        return
    if "8" in S:
        print("Yes")
        return
    if len(S) < 2:
        print("No")
        return
    for i in range(10, 100, 8):
        if str(i)[0] in S and str(i)[1] in S:
            print("Yes")
            return
    if len(S) < 3:
        print("No")
        return
    for i in range(100, 1000, 8):
        if str(i)[0] in S and str(i)[1] in S and str(i)[2] in S:
            print("Yes")
            return
    print("No")
