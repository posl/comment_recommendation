def main():
    S = input()
    S_list = list(S)
    S_list.reverse()
    S_reverse = "".join(S_list)
    count = 0
    for i in range(len(S)):
        if S[i] != S_reverse[i]:
            count += 1
    print(count//2)
