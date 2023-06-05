def problem258_a():
    K = int(input())
    H = K // 60 + 21
    M = K % 60
    if M < 10:
        print(str(H) + ':0' + str(M))
    else:
        print(str(H) + ':' + str(M))

if __name__ == '__main__':
    problem258_a()