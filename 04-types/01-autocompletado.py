def get_full_name(first_name, last_name):
    # .title() es un método de los strings que pone la primera letra de cada palabra en mayúscula.
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("gian", "paucar"))



# print(get_full_name("Jose", 0)) # Esto genera error por el 0

# AttributeError: 'int' object has no attribute 'title'
# significa que estás intentando usar el método .title() sobre un número entero (int),
#  pero ese método solo existe para strings.