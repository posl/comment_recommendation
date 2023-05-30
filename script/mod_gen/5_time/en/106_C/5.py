def main():
    S = input()
    K = int(input())
    for i in range(len(S)):
        if S[i] != '1':
            print(S[i])
            break
        elif K == i+1:
            print(1)
            break
main()
