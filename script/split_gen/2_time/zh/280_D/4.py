def get_prime_list(n):
    """获取2-n之间的素数"""
    if n<2:
        return []
    prime_list=[]
    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            prime_list.append(i)
    return prime_list
