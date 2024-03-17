#Jaunel Deans
#September 18, 2023
import time

#Intro
name = input("Hello user, what is your name? ")
print("Well, Hello there " + name + ". I hope you are well.")
print()
time.sleep(1.5)
print("I am going to ask you three questions about yourself. Are you ready?")
input()

#Countdown
print()
print("Regardless if you are ready or not, "+ name + " here they come...")
time.sleep(1.5)
print()
print(3)
time.sleep(2)
print(2)
time.sleep(2)
print(1)
time.sleep(2)
print()

print("Here we go, "+ name + ":)")
time.sleep(1.5)
#Question 1, Answer and Response 
#Input
q1 = input("\nWhat are you most afraid of? ")
#Output
print("Don't worry, " + name + " your fear is reasonable.\n\n")
print()
time.sleep(1.75)

#Question 2, Answer and Response 
#Input
q2 = input("Next question, " + name + " how many siblings do you have? ")
#Output
print("I hope you're having fun\n\n")
time.sleep(1.5)
print()

#Question 2, Answer and Response 
#Input
q3 = input("Last Question " + name + ", what are three words that describe you best?")
#Output
print("I hope that wasn't to hard for you, " + name + ".")
time.sleep(1.5)
print()

#Summary
print("Thank you for your answers. Just to recap, you are fearful of " + q1 + ", you have " + q2 + " siblings and three words that describe you are " + q3)

#Outro
print("Thank you for contributing to this questionnaire " + name + ". I hope you have a great life.")
