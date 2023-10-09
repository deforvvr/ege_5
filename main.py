
#polyakov 7
# for N in range(1, 100):
#     b = bin(N)[2:]
#     if b.count('1') % 2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     if b.count('1') % 2 == 0:
#         b += '0'
#     else:
#         b += '1'
#     r = int(b, 2)
#     if r > 125:
#         print(N)
#         break

# for N in range(1, 100):
#     b = bin(N)[2:]
#     if b.count('1') > b.count('0'):
#         b += '1'
#     else:
#         b += '0'
#     r = int(b, 2)
#     if r < 100:
#         print(r)

#universal cod dlya perevoda v ss
# def f(x, k):
#     alf = '0123456789abcdefghij'
#     s = ''
#     while x > 0:
#         s = alf[x % k] + s
#         x = x // k
#     return s


# for N in range(1, 256):
#     b = bin(N)[2:]
#     b = '0' * (8 - len(b)) + b
#     k = b.rfind('1')
#     s = ''
#     for i in range(8):
#         if i < k:
#             if b[i] == '0': s += '1'
#             else: s += '0'
#         else:
#             s += b[i]
#     r = int(s, 2)
#     if r == 98:
#         print(N)



# for N in range(1000, 10000):
#     c1 = int(str(N)[0])
#     c2 = int(str(N)[1])
#     c3 = int(str(N)[2])
#     c4 = int(str(N)[3])
#
#     p1 = c1 + c2
#     p2 = c3 + c4
#
#     if p1 < p2:
#         r = [p2, p1]
#     else:
#         r = [p1, p2]
#     if r == [14, 12]:
#         print(N)
#         break


# for n1 in range(100, 1000):
#     for n2 in range(100, 1000):
#         s1 = int(str(n1)[0]) + int(str(n2)[0])
#         s2 = int(str(n1)[1]) + int(str(n2)[1])
#         s3 = int(str(n1)[2]) + int(str(n2)[2])
#         r = [s1, s2, s3]
#         r.sort()
#
#         if r[::-1] == [13, 10, 7] and (n1 == 486 or n2 == 486):
#             print(n1, n2)


# for i in range(1000, 10000):
#     s1 = int(str(i)[0]) + int(str(i)[1])
#     s2 = int(str(i)[1]) + int(str(i)[2])
#     s3 = int(str(i)[2]) + int(str(i)[3])
#     mini = min(s1, s2, s3)
#     if s1 == mini:
#         r = [s2, s3]
#     if s2 == mini:
#         r = [s1, s3]
#     if s3 == mini:
#         r = [s2, s1]
#     r.sort()
#     if r[::-1] == [15, 14]:
#         print(i)
#         break


# for n in range (1, 100):
#     b = bin(n)[2:]
#     b1 = b + b[-1]
#     if b.count('1') % 2 == 0:
#         b1 += '0'
#     else:
#         b1 += '1'
#     if b1.count('1') % 2 != 0:
#         b1 += '1'
#     else:
#         b1 += '0'
#     r = int(b1, 2)
#     if r > 80:
#         print(r)
#         break

a = []
for i in range(100, 1000):
    c1 = int(str(i)[0])
    c2 = int(str(i)[1])
    c3 = int(str(i)[2])
    maxi = c1 + c2
    mini = c1 + c2
    if c1 + c3 > maxi:
        maxi = c1 + c3
    if c2 + c3 > maxi:
        maxi = c2 + c3
    if c1 + c3 < mini:
        mini = c1 + c3
    if c2 + c3 < mini:
        mini = c2 + c3
    if maxi - mini == 58:
        a.append(i)
print(len(a))