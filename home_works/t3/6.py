a = int(input())
m5 = 0
f = 0
for b in range(0, a + 1, 5):
    m5 += b
for i in range(1, a + 1, 2):
    f += i
print(f * m5)
