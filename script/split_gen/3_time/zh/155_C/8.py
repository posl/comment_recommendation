def main():
    N = input()
    S = []
    for i in range(int(N)):
        S.append(input())
    S.sort()
    max = 0
    count = 1
    for i in range(int(N)-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max:
        max = count
    count = 1
    for i in range(int(N)-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            if count == max:
                print(S[i])
            count = 1
    if count == max:
        print(S[int(N)-1])
