>>> word = ['cat', 'window', 'defenstrate', 'world']
>>> for w in word[:]:
...     if len(w) > 4:
...             word.insert(0,w)
...
>>> word
['world', 'defenstrate', 'window', 'cat', 'window', 'defenstrate', 'world']

