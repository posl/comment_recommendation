def get_closest_shrine temples, shrine
  temples.each do |temple|
    if shrine < temple
      return shrine
    end
  end
  return temples.last
end
