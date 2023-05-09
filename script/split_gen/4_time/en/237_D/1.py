def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'R':
            A.append(i+1)
        else:
            A.insert(0, i+1)
    print(*A)
