def main
  n, q = gets.chomp.split(' ').map(&:to_i)
  follow = Array.new(n) { Array.new(n, false) }
  q.times do
    t, a, b = gets.chomp.split(' ').map(&:to_i)
    case t
    when 1
      follow[a - 1][b - 1] = true
    when 2
      n.times do |i|
        follow[a - 1][i] = follow[i][a - 1] if follow[b - 1][i]
      end
    when 3
      n.times do |i|
        n.times do |j|
          follow[i][j] = follow[i][j] || (follow[i][a - 1] && follow[b - 1][j])
        end
      end
    end
  end
  n.times do |i|
    n.times do |j|
      follow[i][j] = follow[i][j] || (follow[i][i] && follow[j][j])
    end
  end
  n.times do |i|
    puts follow[i].map { |v| v ? 'Yes' : 'No' }.join(' ')
  end
end
