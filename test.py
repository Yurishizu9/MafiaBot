script = open('text.txt')

print(script)
script = script.read()
print(script)
print(len(script))
print(script[:6])



for line in 'speedy fredy':
    if 'e' in line:
        # continue skips to the next iteration of the loop 
        # so 'e' is never printed out to the console
        continue
    print(line)



print(dir(type))
print(dir(range))
