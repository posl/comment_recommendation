def lunlun(n):
    if n < 10:
        return [n]
    else:
        ans = []
        for i in range(10):
            if i == n % 10:
                ans += [int(str(n) + str(i))]
            elif i == n % 10 - 1:
                ans += [int(str(n) + str(i))]
            elif i == n % 10 + 1:
                ans += [int(str(n) + str(i))]
        return ans
n = int(input())
lunlun_list = []
for i in range(10):
    lunlun_list += lunlun(i)
lunlun_list.sort()
print(lunlun_list[n - 1])
from collections import deque
K = int(input())
q = deque(range(1, 10))
for i in range(K):
    a = q.popleft()
    if a % 10 != 0:
        q.append(10 * a + a % 10 - 1)
    q.append(10 * a + a % 10)
    if a % 10 != 9:
        q.append(10 * a + a % 10 + 1)
print(a)
from collections import deque
K = int(input())
q = deque(range(1, 10))
for i in range(K):
    a = q.popleft()
    if a % 10 != 0:
        q.append(10 * a + a % 10 - 1)
    q.append(10 * a + a % 10)
    if a % 10 != 9:
        q.append(10 * a + a % 10 + 1)
print(a)
from collections import deque
K = int(input())
q = deque(range(1, 10))
for i in range(K):
    a = q.popleft()
    if a % 10 != 0:
        q.append(10 * a + a % 10 - 1)
    q.append(10 * a + a % 10)
    if a % 10 != 9:
        q.append(10 * a + a % 10 + 1)
print(a)
from collections import deque
K = int(input())
q = deque(range(1, 10))
for i in range(K):
    a = q.popleft()
    if a % 10 != 0:

if __name__ == '__main__':
    lunlun()