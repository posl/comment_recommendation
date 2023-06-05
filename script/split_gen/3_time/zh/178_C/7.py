def main():
    n = int(input())
    print((pow(10,n,10**9+7)-2*pow(9,n,10**9+7)+pow(8,n,10**9+7))%(10**9+7))
