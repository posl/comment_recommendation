def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    result = 'Yes'
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j]:
                result = 'No'
    print(result)
