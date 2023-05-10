def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    S.append("")
    max = 0
    max_name = ""
    now = 0
    for i in range(N):
        if S[i] == S[i+1]:
            now += 1
        else:
            if now > max:
                max = now
                max_name = S[i]
            now = 0
    print(max_name)
