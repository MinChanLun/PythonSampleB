# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# def concat(*args, sep = "/"): #sep = separate
# 	return sep.join(args)

# concat("earth", "mars", "venus")

# concat("earth", "mars", "venus", sep = ".")

# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# d = {"voltage": "1000K voltage", "state": "die or undie", "action": "BOOM"}
# parrot(**d)

# def make_incrementor(n):
# 	return lambda x : x + n

# f = make_incrementor(42)
# f(0)

# f(1)

pairs = [(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')]
pairs.sort(key = lambda pair : pair[2])
pairs
