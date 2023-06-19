def f(m, a_list):
    sum = 0
    for a in a_list:
        sum += m % a
    return sum
N = int(input())
a_list = list(map(int, input().split()))
m_max = max(a_list) * (N - 1)
m_min = min(a_list)
m = (m_max + m_min) // 2
while m_max - m_min > 1:
    if f(m, a_list) > f(m + 1, a_list):
        m_max = m
    else:
        m_min = m
    m = (m_max + m_min) // 2
print(f(m, a_list))
