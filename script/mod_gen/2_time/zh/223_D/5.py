def cal_distance(AB):
    N = len(AB)
    if N == 1:
        return AB[0][0]
    else:
        left = AB[0][0]
        right = AB[N-1][0]
        while left < right:
            mid = (left + right) / 2
            sum = 0
            for i in range(N):
                if mid < AB[i][0]:
                    sum += AB[i][0] - mid
            if sum == mid:
                return mid
            elif sum > mid:
                left = mid
            else:
                right = mid
N = int(raw_input())
AB = []
for i in range(N):
    AB.append(map(int, raw_input().split()))
AB.sort()
print cal_distance(AB)
