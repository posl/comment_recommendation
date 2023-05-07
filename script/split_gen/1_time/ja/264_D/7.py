def main():
    S = input()
    A = 'atcoder'
    count = 0
    for i in range(len(S)):
        if S[i] != A[i]:
            count += 1
    print(count)
