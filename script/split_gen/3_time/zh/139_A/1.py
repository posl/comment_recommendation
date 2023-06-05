def main():
    S = input()
    T = input()
    cnt = 0
    for i in range(3):
        if S[i] == T[i]:
            cnt = cnt + 1
    print(cnt)
