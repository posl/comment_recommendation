def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    result = "Yes"
    for i in range(N):
        if S[i][0] not in ["H","D","C","S"]:
            result = "No"
            break
        if S[i][1] not in ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]:
            result = "No"
            break
        for j in range(i):
            if S[i] == S[j]:
                result = "No"
                break
    print(result)
    return
