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

if __name__ == '__main__':
    solve()