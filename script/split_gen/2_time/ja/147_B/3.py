def main():
    S = input()
    cnt = 0
    for i in range(len(S)//2):
        if S[i] != S[-1-i]:
            cnt += 1
    print(cnt)
