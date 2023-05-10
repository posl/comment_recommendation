Synthesizing 10/10 solutions

=======
Suggestion 1

def swap_array(a, p, q, r, s):
    b = a.copy()
    b[p-1:q] = a[r-1:s]
    b[r-1:s] = a[p-1:q]
    return b

=======
Suggestion 2

def get_input():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    return N, P, Q, R, S, A

=======
Suggestion 3

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[0:p-1] + a[r-1:s] + a[q-1:r-1] + a[p-1:q-1] + a[s:n]
    print(' '.join(map(str, b)))

=======
Suggestion 4

def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input()
    input_line = input_line.split(" ")
    N = int(input_line[0])
    P = int(input_line[1])
    Q = int(input_line[2])
    R = int(input_line[3])
    S = int(input_line[4])
    input_line = input()
    input_line = input_line.split(" ")
    A = []
    for i in range(N):
        A.append(int(input_line[i]))
    # print(N, P, Q, R, S)
    # print(A)
    B = []
    for i in range(N):
        if i >= P-1 and i <= Q-1:
            B.append(A[i+R-Q])
        elif i >= R-1 and i <= S-1:
            B.append(A[i+P-R])
        else:
            B.append(A[i])
    # print(B)
    for i in range(N):
        if i == N-1:
            print(B[i])
        else:
            print(B[i], end="")

=======
Suggestion 5

def swap_array(p,q,r,s,array)
  temp1 = array[p-1..q-1]
  temp2 = array[r-1..s-1]
  array[p-1..q-1] = temp2
  array[r-1..s-1] = temp1
  return array
end

n,p,q,r,s = gets.chomp.split.map(&:to_i)
array = gets.chomp.split.map(&:to_i)
puts swap_array(p,q,r,s,array).join(" ")

=======
Suggestion 6

def swap_array(array, p, q, r, s):
    array1 = array[:p-1]
    array2 = array[p-1:q]
    array3 = array[q:r]
    array4 = array[r:s]
    array5 = array[s:]

    return array1 + array3 + array2 + array5 + array4

=======
Suggestion 7

def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A[:P-1] + A[R-1:S] + A[Q:S-1] + A[P-1:Q-1] + A[S:]
    print(*B)

=======
Suggestion 8

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[P-1:Q] + A[R-1:S]
    A[P-1:Q] = B[R-P:S-P]
    A[R-1:S] = B[0:Q-P] + B[Q-P:]
    print(*A)

=======
Suggestion 9

def swap(array, p, q, r, s):
    tmp = array[p-1:q]
    array[p-1:q] = array[r-1:s]
    array[r-1:s] = tmp
    return array

=======
Suggestion 10

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b
