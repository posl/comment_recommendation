def follow(x, y)
  if $follow[x].include?(y)
    puts "Yes"
  else
    puts "No"
  end
end
