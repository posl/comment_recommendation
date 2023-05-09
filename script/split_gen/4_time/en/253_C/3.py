def main():
    N = int(input())
    S = []
    for i in range(N):
        line = input().split()
        if line[0] == '1':
            S.append(int(line[1]))
        elif line[0] == '2':
            x = int(line[1])
            c = int(line[2])
            for j in range(c):
                if x in S:
                    S.remove(x)
                else:
                    break
        elif line[0] == '3':
            print(max(S)-min(S))
