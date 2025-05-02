def get_count(sentence):
    V = ["a", "e", "i", "o", "u"]
    s = 0
    for v in V:
   		s+= sentence.count(v)
    return s
