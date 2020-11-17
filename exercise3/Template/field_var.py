
def field_var(value, x, y):
    #there is the value value in field x y
    assert type(value) == int and int(value) != 0 and type(x) == int and type(y) == int
    return "V%i%i%i" % (value, x, y)