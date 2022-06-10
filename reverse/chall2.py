from dis import dis
from marshal import load

key = "d1j#H(&Ja1_2 61fG&"
tmp = [292, 194, 347, 382, 453, 276, 577, 434, 183, 295, 318, 196,
       482, 325, 412, 502, 396, 402, 328, 194, 473, 490, 299, 503,
       386, 215, 263, 211, 318, 206, 533]
n = len(tmp)


def bytecode2asm():
    """Convert the pyc file (python bytecodes) to a asm file."""
    with open("chall2.pyc", 'rb') as f:
        f.seek(16)
        dis(load(f), file=open("chall2.asm"))


def listcomp(l):
    out = []
    for e in l:
        out += ord(e)
    return out


def code(l):
    if not isinstance(l, str):
        if len(l) >= 1:
            [el, *rest] = l
            # STACK 36 => 5*el | ord | key | len | rest
            # STACK 44 => 5*el | ord | key | len(rest) | len(key)
            # STACK 50 => 5*el | ord(key[len(rest) % len(key)])
            # STACK 54 => [5*el ^ ord(key[len(rest) % len(key)])]
            a = 5*el
            b = ord(key[len(rest) % len(key)])
            return [a ^ b] + code(rest)
    if not isinstance(l, str):
        if len(l) == 0:
            return []
    return None


def chall2():
    userInput = listcomp(iter(input("Password:")))
    if code(userInput) == tmp:
        print("Bravo")
        return None

    print("Dommage...")
    return None


def computeB():
    return [ord(key[(n-1-i) % len(key)]) for i in range(n)]


def reverse():
    print(''.join([chr((x ^ y)//5) for x, y in zip(tmp, computeB())]))


if __name__ == "__main__":
    reverse()
