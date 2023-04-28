Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        if A[i] > 10:
            ans += A[i] - 10

    print(ans)

=======
Suggestion 2

def harvest(n, a):
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    return ans

=======
Suggestion 3

def harvest(n, a)
  sum = 0
  a.each do |i|
    if i > 10
      sum += i - 10
    end
  end
  sum
end

n = gets.to_i
a = gets.split.map(&:to_i)
puts harvest(n, a)

=======
Suggestion 4

def harvest(N, A):
    result = 0
    for i in range(N):
        if A[i] > 10:
            result += A[i] - 10
    return result

=======
Suggestion 5

def harvest_apple():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    return ans

=======
Suggestion 6

def harvest_fruits(N, A):
    sum = 0
    for i in range(N):
        if A[i] > 10:
            sum += A[i] - 10
    return sum

=======
Suggestion 7

def solve(n, a)
  ans = 0
  a.each do |i|
    if i > 10
      ans += i - 10
    end
  end
  ans
end

n = gets.chomp.to_i
a = gets.chomp.split(" ").map(&:to_i)
puts solve(n, a)

=======
Suggestion 8

def f204_b(n, a):
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    return ans

=======
Suggestion 9

def harvest():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)
    a_list = [a for a in a_list if a > 10]
    return sum(a_list) - len(a_list) * 10

print(harvest())

=======
Suggestion 10

def get_input_line():
    return input()
