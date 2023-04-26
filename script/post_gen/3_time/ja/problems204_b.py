Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if a[i] > 10:
            sum += a[i] - 10
    print(sum)

=======
Suggestion 3

def harvest(n, a)
  sum = 0
  a.each do |i|
    if i > 10
      sum += i - 10
    end
  end
  return sum
end

n = gets.to_i
a = gets.chomp.split.map(&:to_i)
puts harvest(n, a)

=======
Suggestion 4

def harvest(n, a):
    count = 0
    for i in range(n):
        if a[i] > 10:
            count += a[i] - 10
    return count

=======
Suggestion 5

def harvest():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i > 10:
            count += i - 10
    print(count)

=======
Suggestion 6

def harvest(a):
    if a <= 10:
        return 0
    else:
        return a-10

n = int(input())
a = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += harvest(a[i])

print(sum)

=======
Suggestion 7

def harvest(n,a):
    result = 0
    for i in range(n):
        if a[i] > 10:
            result += a[i] - 10
    return result

=======
Suggestion 8

def harvest(N, A):
    sum = 0
    for i in range(N):
        if A[i] >= 10:
            sum += A[i] - 10
    return sum

=======
Suggestion 9

def harvest(trees):
    result = 0
    for tree in trees:
        if tree > 10:
            result += tree - 10
    return result

=======
Suggestion 10

def get_input_data():
    n = int(input())
    a_list = list(map(int, input().split()))
    return n, a_list
