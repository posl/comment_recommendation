def problems150_b():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

if __name__ == '__main__':
    problems150_b()