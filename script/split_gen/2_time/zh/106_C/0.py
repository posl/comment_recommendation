def main():
    S = input()
    K = int(input())
    n = len(S)
    i = 0
    while i < n and int(S[i]) == 1:
        i += 1
    if i == n:
        print(1)
    elif K <= i:
        print(1)
    else:
        print(S[i])
main()
