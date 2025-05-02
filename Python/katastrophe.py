def strong_enough(earthquake, age):
	strenght = 1000
	for i in range (0, age):
		strenght *= (99/100)
	return "Safe!" if (sum(earthquake[0]) * sum(earthquake[1]) * sum(earthquake[2])<= strenght) else "Needs Reinforcement!"
