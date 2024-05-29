print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
totalname = lower_name1 + lower_name2

t = totalname.count("t")
r = totalname.count("r")
u = totalname.count("u")
e = totalname.count("e")

true = t + r + u + e

l = totalname.count("l")
o = totalname.count("o")
v = totalname.count("v")
e = totalname.count("e")

love = l + o + v + e

true_love = str(true) + str(love)
love_score = int(true_love)


if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}")
















