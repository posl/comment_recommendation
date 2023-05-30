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
