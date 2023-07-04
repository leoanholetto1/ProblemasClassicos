from secrets import token_bytes
from typing import Tuple
from typing import List


def randon_key(length: int)-> int:
    tb: bytes = token_bytes(length)
    return  int.from_bytes(tb,"big")

def encrypt(original: str) -> Tuple[int,int]:
    original_bytes: bytes = original.encode()
    dummy: int =  randon_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes,"big")
    encrypted: int = original_key ^ dummy
    return dummy,encrypted

def decrypt(key1:int,key2:int) -> str:
    decrypted:int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7)//8,"big")
    return  temp.decode()

if __name__ == "__main__":
    lista: List[int] = []
    for i in range(1,4):
        lista2: List[int] = []
        for j in range(1,4):
            lista2.append(i*j)
        lista.append(lista2)
    key1,key2 = encrypt(str(lista))
    result: str = decrypt(key1,key2)
    print(result)