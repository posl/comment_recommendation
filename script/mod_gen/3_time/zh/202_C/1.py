def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #B中的元素作为key，B中元素出现的次数作为value存储在字典中
    B_dict = {}
    for i in range(N):
        if B[i] in B_dict:
            B_dict[B[i]] += 1
        else:
            B_dict[B[i]] = 1
    #C中的元素作为key，C中元素出现的次数作为value存储在字典中
    C_dict = {}
    for i in range(N):
        if C[i] in C_dict:
            C_dict[C[i]] += 1
        else:
            C_dict[C[i]] = 1
    #C中的元素作为key，C中元素出现的次数作为value存储在字典中
    A_dict = {}
    for i in range(N):
        if A[i] in A_dict:
            A_dict[A[i]] += 1
        else:
            A_dict[A[i]] = 1
    #A_dict中的key作为B_dict的key，A_dict中的value乘以B_dict中的value作为最终的value
    #A_dict中的key作为C_dict的key，A_dict中的value乘以C_dict中的value作为最终的value
    #如果A_dict中的key在B_dict和C_dict中都存在，那么最终的value是上面两种情况相加
    result = 0
    for key in A_dict:
        if key in B_dict and key in C_dict:
            result += A_dict[key] * B_dict[key] * C_dict[key]
    print(result)

if __name__ == '__main__':
    main()