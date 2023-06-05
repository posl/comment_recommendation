def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    a.append(0)
    b.append(0)
    a_index = n
    b_index = m
    a_time = 0
    b_time = 0
    while a_time+b_time<k:
        if a_time+b_time+a[a_index]>k:
            a_time = k - b_time
            break
        if a_time+b_time+b[b_index]>k:
            b_time = k - a_time
            break
        if a[a_index]>b[b_index]:
            b_time += b[b_index]
            b_index -= 1
        else:
            a_time += a[a_index]
            a_index -= 1
    print(a_index+b_index)
main()
