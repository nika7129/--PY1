import random
symbol = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def get_random_password(password, p=8) -> str:
    for n in range(password):
        passw = ''
        for n in range(p):
            passw += random.choice(symbol)
        return passw
print(get_random_password(1))
