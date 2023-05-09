def solve():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == "v":
            if i == 0:
                continue
            if S[i - 1] == "w":
                count += 1
    print(count)
