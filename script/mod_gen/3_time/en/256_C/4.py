def solve(h1,h2,h3,w1,w2,w3):
    cnt = 0
    for i1 in range(1,31):
        for i2 in range(1,31):
            for i3 in range(1,31):
                for j1 in range(1,31):
                    for j2 in range(1,31):
                        for j3 in range(1,31):
                            if (i1+i2+i3 == h1) and (i1+i2+i3 == h2) and (i1+i2+i3 == h3) and (j1+j2+j3 == w1) and (j1+j2+j3 == w2) and (j1+j2+j3 == w3) and (i1+j1 == i2+j2) and (i2+j2 == i3+j3) and (i1+j1 == i3+j3):
                                cnt += 1
    return cnt
h1,h2,h3,w1,w2,w3 = map(int,input().split())
print(solve(h1,h2,h3,w1,w2,w3))
I tried to write a code with nested for loops, but it was too slow. I want to know if there is a more efficient way to solve this problem.
I think there is no efficient way to solve this problem. I think the best way to solve this problem is to use brute force. And I think that the time complexity of this code is O(n^6).
I think there is no efficient way to solve this problem. I think the best way to solve this problem is to use brute force. And I think that the time complexity of this code is O(n^6).
I agree with you. I think that the time complexity of this code is O(n^6).
I think there is no efficient way to solve this problem. I think the best way to solve this problem is to use brute force. And I think that the time complexity of this code is O(n^6).
I agree with you. I think that the time complexity of this code is O(n^6).
I think there is no efficient way to solve this problem. I think the best way to solve this problem is to use brute force. And I think that the time complexity of this code is O(n^6).
I agree with you. I think that the time complexity of this code is

if __name__ == '__main__':
    solve()