Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def follow_check(follow, a, b)
  if follow[a] == nil
    return false
  else
    if follow[a].include?(b)
      return true
    else
      return false
    end
  end
end

=======
Suggestion 3

def check_follow(follows, a, b)
  if follows[a].include?(b)
    puts "Yes"
  else
    puts "No"
  end
end

=======
Suggestion 4

def follow(x, y)
  if @follow[x].include?(y) && @follow[y].include?(x)
    puts 'Yes'
  else
    puts 'No'
  end
end

=======
Suggestion 5

def follow(a, b)
  if @follows[a].include?(b)
    puts 'Yes'
  else
    puts 'No'
  end
end

=======
Suggestion 6

def follow(x, y)
  if $follow[x].include?(y)
    puts "Yes"
  else
    puts "No"
  end
end

=======
Suggestion 7

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

=======
Suggestion 8

def follow?(a, b)
  return false if @follows[a].nil? || @follows[a].empty?
  return @follows[a].include?(b)
end

=======
Suggestion 9

def follow(user1, user2, follow_list):
    if user1 in follow_list[user2]:
        return True
    else:
        return False

=======
Suggestion 10

def follow(x, y, user)
  if user[x] == nil
    user[x] = []
  end
  user[x] << y
end
