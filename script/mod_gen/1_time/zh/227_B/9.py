def problems227_b(N):
    S = []
    for i in range(N):
        S.append(int(input()))
    count = 0
    for i in range(N):
        a = 1
        while a * a <= S[i]:
            if S[i] % a == 0:
                b = S[i] // a
                if 4 * a * b + 3 * a + 3 * b == S[i]:
                    break
            a += 1
        if a * a > S[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    problems227_b()