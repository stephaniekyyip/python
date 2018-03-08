import random

random.seed()

rand = random.randint(1, 100)

guess = 0

while (guess != rand):
  guess = input("Guess a number from 1 to 100: ")

  if guess > rand:
    print "Too high. Try again."
  elif guess < rand:
    print "Too low. Try again."

print "Correct!"