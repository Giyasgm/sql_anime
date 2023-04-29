import random

a1 = ["Akane", 56, 157, "pink", "C"]
a2 = ["Hana", 28, 151, "yellow", "D"]
a3 = ["Haruka", 67, 164, "black", "F"]
a4 = ["Hikari", 35, 150, "pink", "A"]
a5 = ["Hinata", 21, 168, "white", "E"]
a6 = ["Kagura", 23, 162, "orange", "B"]
a7 = ["Kaori", 100, 161, "blue", "B"]
a8 = ["Kyoko", 74, 178, "white", "A"]
a9 = ["Nagisa", 82, 175, "red", "C"]
a10 = ["Rei", 60, 155, "pink", "B"]
a11 = ["Rin", 66, 162, "orange", "F"]
a12 = ["Sakura", 35, 176, "yellow", "E"]
a13 = ["Shizuka", 78, 158, "pink", "C"]
a14 = ["Yuuki", 17, 163, "silver", "D"]
a15 = ["Yumi", 85, 171, "white", "D"]
aa = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]
aa2 = set()
aa3 = set()

for i in aa:
    aa3.add(i[4])

for i in aa:
    aa2.add(i[3])

# for i in range(15):
#     print(random.randint(16, 100))

# for i in range(15):
#     print(random.randint(150, 180))
#
# colors = ["red", "blue", "green", "yellow", "purple", "pink", "orange", "brown", "black", "white", "gray", "gold", "silver"]
#
# for i in range(15):
#     print(colors[random.randint(0, len(colors)-1)])

# bra = ["A", "B", "C", "D", "E", "F"]
#
# for i in range(15):
#     print(bra[random.randint(0, len(bra)-1)]))
