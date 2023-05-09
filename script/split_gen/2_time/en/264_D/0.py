def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] != "atcoder"[i]:
            count += 1
    print(count)
