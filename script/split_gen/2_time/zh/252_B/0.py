def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # print(n,k,a,b)
    print('Yes' if len(set(a) & set(b)) > 0 else 'No')
