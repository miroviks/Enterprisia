import hashlib

from server import check, give_salt

class client:
    def __init__(self, login, name):
        self.login = login
        self.name = name

salt = give_salt()
login = hashlib.scrypt(b'Stas', salt = salt, n = 16, r = 512, p = 16).hex()
passw = hashlib.scrypt(b'123', salt = salt, n = 16, r = 512, p = 16).hex()


sp = check(login, passw)

if len(sp) > 0:
    client = client(sp[0], sp[1])