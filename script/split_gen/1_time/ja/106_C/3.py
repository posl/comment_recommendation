def main():
    S = input()
    K = int(input())
    count = 0
    for i in S:
        if i == "1":
            count += 1
        else:
            break
    if count >= K:
        print(1)
    else:
        print(S[count])
