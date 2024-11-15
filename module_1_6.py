my_dict = {"Den" : 1995,
           "Max": 1994,
           "Jhon": 1992}
print (my_dict)
print (my_dict ["Den"])
print (my_dict.get ("Alex"))
my_dict.update ({"Mark": 1990,
                 "Ann": 1996})
x = my_dict.pop ("Max")
print (x)
print (my_dict)

my_set = {1, 2 , 3, "car", "plane", 2, 4, 5, "car"}
print (my_set)
print (my_set.update(['ship', 6]))
my_set.discard (2)
print (my_set)