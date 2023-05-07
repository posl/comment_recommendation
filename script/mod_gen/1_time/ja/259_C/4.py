def main():
    S = input()
    T = input()
    ans = 'Yes'
    for i in range(len(T)):
        if T[i] != S[i]:
            if T[i] != S[i+1]:
                ans = 'No'
                break
    print(ans)

if __name__ == '__main__':
    main()