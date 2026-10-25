import hashlib, binascii

def gen(password,salt_hex):
    salt = binascii.unhexlify(salt_hex)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 10000, dklen=32)
    return dk.hex(), salt.hex()

for p,salt in [
    ('Admin@2026','d5aee5627d95f381a1b1a1d5357a7f0f'),
    ('Passenger1!','9acd84f91d5f114a7d9a6dd111e4e1a3'),
    ('Passenger2!','1d2574a229f8dd3df32c4f965ab360cc'),
    ('Passenger3!','a1ea4ec59e6c3d0d7fca08239f4b1d1b'),
    ('Admin123!','64a4d7cab4bdcaac7d2d57c4d90f9f0d'),
]:
    h,s = gen(p,salt)
    print(p, 'salt=', s, 'hash=', h)
