def main():
    N,K = map(int,input().split())
    V = list(map(int,input().split()))
    max_sum = 0
    for i in range(0,min(N,K)+1):
        for j in range(0,min(N,K)-i+1):
            left = V[:i]
            right = V[N-j:]
            if len(left) > 0:
                left.sort()
                for k in range(0,min(len(left),K-i-j)):
                    if left[k] < 0:
                        left[k] = 0
                    else:
                        break
            if len(right) > 0:
                right.sort(reverse=True)
                for k in range(0,min(len(right),K-i-j)):
                    if right[k] < 0:
                        right[k] = 0
                    else:
                        break
            if len(left) > 0:
                left.sort(reverse=True)
                max_sum = max(max_sum,sum(left[:K-i-j])+sum(right[:K-i-j]))
            else:
                max_sum = max(max_sum,sum(right[:K-i-j]))
    print(max_sum)
