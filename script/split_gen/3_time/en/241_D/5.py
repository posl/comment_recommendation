def main():
    N = int(input())
    A = []
    for i in range(N):
        s = input().split()
        if s[0] == '1':
            A.append(int(s[1]))
        elif s[0] == '2':
            x = int(s[1])
            k = int(s[2])
            B = [a for a in A if a <= x]
            if len(B) < k:
                print(-1)
            else:
                print(sorted(B)[-k])
        else:
            x = int(s[1])
            k = int(s[2])
            B = [a for a in A if a >= x]
            if len(B) < k:
                print(-1)
            else:
                print(sorted(B)[k-1])
