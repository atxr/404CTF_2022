a = open('disk0.img', 'rb').read()
b = open('disk1.img', 'rb').read()
k = 0
c = []
while k < len(a):
    c += bytes([a[k] ^ b[k]])
    k += 1

d = b''
z = [a, b, c]
j = 2
for k in range(len(a)):
    zz = []
    for i in range(3):
        if i != j:
            zz.append(z[i])
    d += bytes([zz[0][k]]) + bytes([zz[1][k]])
    j = (j-1) % 3
open('flag.zip', 'wb').write(d)
