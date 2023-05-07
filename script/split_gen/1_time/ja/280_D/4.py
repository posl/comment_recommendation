def main():
    K = int(input())
    N = 1
    while K > 1:
        if K % 2 == 0:
            K = K // 2
        elif K % 5 == 0:
            K = K // 5
        else:
            break
        N += 1
    print(N)
