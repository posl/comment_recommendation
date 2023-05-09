def main():
    S = input()
    K = int(input())
    S = S + "X"
    S_list = []
    count = 0
    for i in range(len(S)):
        if S[i] == "X":
            if count != 0:
                S_list.append(count)
                count = 0
        else:
            count += 1
    if len(S_list) <= K:
        print(len(S) - 1)
    else:
        S_list.sort()
        print(len(S) - 1 - sum(S_list[:K]))
