def swap(p, q, r, s, list):
    list1 = list[0:p]
    list2 = list[p:q]
    list3 = list[q:r]
    list4 = list[r:s]
    list5 = list[s:]
    list2.extend(list4)
    list2.extend(list3)
    list2.extend(list5)
    list1.extend(list2)
    return list1
N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = swap(P-1, Q, R, S+1, A)
print(*B)

if __name__ == '__main__':
    swap()