def main():
    S = input()
    K = int(input())
    s = 0
    for i in range(len(S)):
        if S[i] == '1':
            s += 1
        else:
            break
    if K <= s:
        print(1)
    else:
        print(S[s])
