def get_friends_secret(N,X,A):
    # 朋友列表
    friend_list = [0] * N
    # 朋友是否知道秘密
    friend_list[X-1] = 1
    # 朋友是否已经分享秘密
    friend_list_shared = [0] * N
    # 朋友已经知道秘密的个数
    friend_secret_num = 1
    while friend_secret_num < N:
        for i in range(N):
            if friend_list[i] == 1 and friend_list_shared[i] == 0:
                friend_list_shared[i] = 1
                if friend_list[A[i]-1] == 0:
                    friend_list[A[i]-1] = 1
                    friend_secret_num += 1
    return friend_secret_num
