def main():
    S = input()
    count = 0
    for i in range(len(S)):
        for j in range(len(S)):
            if i != j:
                if S[i] == S[j]:
                    count += 1
    if count == 0:
        print(S[0])
    elif count == 1:
        print(S[1])
    else:
        print(-1)
