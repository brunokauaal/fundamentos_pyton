#slicing = Crie uma  substring em extraindo elmentos de outra string
#      op de= indexação  indexing[] or slice() = paara criar um objeto de fatia
#                               [start:stop:step]


name = "Bruno Carvalho"

first_name = name [0:5:]
last_name = name [6:14]
funky_name= name [0:14:2]
reversed_name= name [::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website= "https://www.linkedin.com/in/bruno-kaua/"

slice = slice(12,-19)


print(website[slice])