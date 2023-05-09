def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i] == '"':
            count += 1
            if count % 2 == 0:
                print('.',end='')
            else:
                print('"',end='')
        else:
            if count % 2 == 0:
                print(S[i],end='')
            else:
                print('.',end='')
    print()
