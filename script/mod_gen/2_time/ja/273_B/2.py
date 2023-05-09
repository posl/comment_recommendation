def round_down(num, divisor):
    return num - (num%divisor)
X,K = map(int,input().split())
for i in range(K):
    X = round_down(X,10**i)
print(X)

if __name__ == '__main__':
    round_down()