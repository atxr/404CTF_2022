f = [88, 1, 140, 1, 203, 208, 89, 207, 132, 191, 178, 110, 138,
     132, 210, 1, 140, 156, 138, 140, 191, 187, 89, 89, 187, 1,
     208, 231, 161, 235, 178, 188, 187, 132, 187]

d = [159, 44, 176, 145, 103, 133, 49, 97, 113, 136, 184, 60, 85,
     69, 64, 186, 182, 37, 56, 170, 19, 108, 152, 183, 41, 197,
     252, 77, 35, 127, 198, 43, 148, 48, 46, 62, 15, 139, 95, 9,
     38, 73, 160, 175, 226, 254, 129, 211, 132, 7, 90, 208, 187,
     164, 158, 201, 116, 93, 54, 87, 126, 128, 16, 50, 244, 12, 4,
     188, 166, 59, 235, 28, 199, 92, 216, 192, 231, 51, 61, 39,
     220, 180, 204, 210, 178, 75, 17, 91, 143, 94, 34, 70, 222,
     125, 131, 195, 33, 223, 242, 156, 232, 140, 67, 24, 111, 141,
     162, 66, 45, 207, 138, 202, 89, 122, 191, 1, 110, 203, 241,
     196, 82, 72, 76, 161, 117, 88, 105, 147, 119, 6, 157, 249,
     168, 81, 32, 224, 237, 5, 146, 27, 80, 57, 42, 102, 172, 219,
     114, 8, 31, 26, 238, 30, 212, 106, 221, 240, 118, 149, 165,
     65, 83, 154, 151, 96, 36, 253, 250, 100, 74, 21, 189, 169,
     239, 142, 173, 217, 181, 86, 29, 68, 155, 115, 225, 135, 0,
     130, 101, 112, 206, 185, 227, 245, 18, 58, 243, 137, 20, 99,
     3, 2, 233, 22, 55, 11, 13, 214, 84, 200, 47, 190, 205, 209,
     53, 194, 229, 171, 248, 230, 109, 234, 236, 98, 213, 247, 150,
     104, 79, 134, 71, 144, 25, 218, 107, 179, 124, 167, 251, 14,
     78, 193, 40, 163, 123, 10, 246, 120, 23, 174, 63, 153, 228,
     52, 121, 177, 215]


def reverse2():
    inp = input()
    s = True
    n = ''
    p = ''

    if inp == '':
        print("Nope")
        return s  # ?

    for k in range(len(inp)):
        # STACK
        # 70 => n | inp | int | len | inp
        # 74 => n | inp | int | len(inp) | k
        # 82 => n | inp | int(len(inp) - k - 1)
        # 82 => n | inp[int(len(inp) - k - 1)]
        n += inp[int(len(inp)) - k - 1]

    for i in range(len(inp)):
        # STACK
        # 128 => p | chr | d | int | ord | n | i
        # 134 => p | chr | d | int(ord(n[i]))
        p += chr(d[int(ord(n[i]))])

    for j in range(len(f)):
        # STACK
        # 172 => f[j] | ord | p[j]
        if f[j] != ord(p[j]):
            continue
        print("Nope")
        return False  # ?

    return s

"""
To return True we must have
f[i] == ord(p[i]) == d[ord(n[i])]
"""
if __name__ == "__main__":
    nrev = ''.join([chr(d.index(el)) for el in f][::-1])
    print(nrev)
