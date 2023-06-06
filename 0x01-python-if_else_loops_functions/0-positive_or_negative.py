#!/usr/bin/env python3

import random

number = random.randint(-10000, 10000)

print(number, "is", end=" ")

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
