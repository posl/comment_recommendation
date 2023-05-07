def nextConfusingTime(h, m)
  if h < 10
    h = "0" + h.to_s
  else
    h = h.to_s
  end
  if m < 10
    m = "0" + m.to_s
  else
    m = m.to_s
  end
  time = h + m
  time = time.split("").map(&:to_i)
  if (time[0] == time[1] && time[2] == time[3]) || (time[0] == time[2] && time[1] == time[3])
    puts "#{h} #{m}"
  else
    if time[2] == 5
      time[2] = 0
      time[3] += 1
    else
      time[2] += 1
    end
    if time[3] == 10
      time[3] = 0
      time[2] += 1
    end
    if time[2] == 10
      time[2] = 0
      time[1] += 1
    end
    if time[1] == 6
      time[1] = 0
      time[0] += 1
    end
    if time[0] == 2 && time[1] == 4
      time[0] = 0
      time[1] = 0
    end
    if time[0] == 0
      puts "0#{time[1]} #{time[2]}#{time[3]}"
    elsif time[1] == 0
      puts "#{time[0]}0 #{time[2]}#{time[3]}"
    elsif time[2] == 0
      puts "#{time[0]}#{time[1]} 0#{time[3]}"
    elsif time[3] == 0
      puts "#{time[0]}#{time[1]} #{time[2]}0"
    else
      puts "#{time[0]}#{time[1]} #{time[2]}#{time[3]}"
    end
  end
end
h, m = gets.chomp.split(" ").map(&:to_i)
nextConfusingTime(h, m)
I'm not sure if this is the best way to solve this
