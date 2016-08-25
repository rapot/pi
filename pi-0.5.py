f = open('pitext.txt', 'w')

f.write(input('Введите числа: '))
f.close()

with open('pi.txt') as fp:
    pi = fp.read()

l = c = 0
with open('pitext.txt') as f:
    for n, i, j in zip(range(1, len(pi) + 1), f.readline(), pi):
        if i == j:
            c += 1
        else:
            print(':( [%d] %s -> %s' % (n, i, j))
            l += 1
print ('---\n:) - %d\n:( - %d' % (c, l))