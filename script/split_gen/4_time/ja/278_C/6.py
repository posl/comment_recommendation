def check_follow(user, follow, followed)
  if follow[user] && follow[user].include?(followed)
    puts 'Yes'
  else
    puts 'No'
  end
end
n, q = gets.split.map(&:to_i)
follow = Hash.new { |h, k| h[k] = [] }
followed = Hash.new { |h, k| h[k] = [] }
q.times do
  t, a, b = gets.split.map(&:to_i)
  case t
  when 1
    follow[a] << b
    followed[b] << a
  when 2
    followed[a].each do |f|
      follow[f] << b
      followed[b] << f
    end
    follow[a] = []
  when 3
    check_follow(a, follow, b)
  end
end
