def main():
    n,k = map(int,input().split())
    result = 0
    for i in range(1,n+1):
        if i >= k:
            result += 1/n
        else:
            result += (1/n)*(1/2)**(i.bit_length()-1)
    print(result)
main()
