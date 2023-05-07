def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    H.append(0)
    for i in range(N):
        if H[i] - H[i+1] > 1:
            print("No")
            break
        elif H[i] - H[i+1] == 1:
            H[i+1] += 1
    else:
        print("Yes")

if __name__ == '__main__':
    main()