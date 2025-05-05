def content_weight(bottle_weight, scale): 
    scale = scale.split(" ")
    times = int(scale[0])
    if scale[2] == "larger":
        part = bottle_weight / (times+1)
        return part * times
    else:        
        part = bottle_weight / (times+1)
        return part
