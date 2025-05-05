def content_weight(bottle_weight, scale): 
    scale = scale.split(" ")
    times = int(scale[0])
    part = bottle_weight / (times+1)
    return part if scale[2] == "smaller" else part * times
