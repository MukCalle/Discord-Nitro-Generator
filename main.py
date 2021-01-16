import random, string

amount =1 int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:1
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GENERATED] {code}')
    value += 1
