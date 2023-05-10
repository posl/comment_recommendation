def main():
    N = input()
    ans = -1
    for i in range(len(N)):
        for j in range(len(N)):
            if i < j:
                continue
            elif i == j:
                if int(N) % 3 == 0:
                    ans = 0
                    break
            else:
                if int(N[:i] + N[j:]) % 3 == 0:
                    if ans == -1:
                        ans = j - i
                    else:
                        ans = min(ans, j - i)
    print(ans)
