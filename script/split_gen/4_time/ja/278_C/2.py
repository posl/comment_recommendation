def check_follow(follows, a, b)
  if follows[a].include?(b)
    puts "Yes"
  else
    puts "No"
  end
end
