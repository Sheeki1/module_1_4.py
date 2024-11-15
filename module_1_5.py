immutable_var = ["cat"], "dog", 1, 2, 3
immutable_var = immutable_var + (11, 12)
immutable_var [0] [0] = "bird"
print ("Immutable tuple:", immutable_var)
mutable_list = [1, 2, 3, "car", "plane"]
mutable_list [1] = 4
mutable_list [3] = "ship"
print ("Mutable list:", mutable_list)