def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(len(S)):
        if S[i] == 'L':
            A.insert(i, i+1)
        else:
            A.insert(i+1, i+1)
    print(*A)
