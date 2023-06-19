def main
  n, m = gets.split.map(&:to_i)
  a = gets.split.map(&:to_i)
  count = 0
  sum = 0
  mod_a = Array.new(m, 0)
  mod_a[0] = 1
  a.each do |ai|
    sum += ai
    mod_a[sum % m] += 1
  end
  mod_a.each do |mod|
    count += mod * (mod - 1) / 2
  end
  puts count
end
main
