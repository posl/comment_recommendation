def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    S.append('')
    max = 0
    max_name = ''
    count = 0
    for i in range(N):
        if S[i] == S[i+1]:
            count += 1
        else:
            if max < count:
                max = count
                max_name = S[i]
            count = 0
    print(max_name)
