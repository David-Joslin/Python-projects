import random

time = [1,2,3,4,5,6,7]
hours = random.choice(time)

subject = ["english","maths","history","irish","french","business","accounting","biology"]
school = random.choice(subject)

txt =("{} hours is good enough for {}").format(hours,school)
print(txt)