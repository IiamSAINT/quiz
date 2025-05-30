
# RECCURSION
#   quiz game
# 2D Lists /Tupples
# Create a Keypad
# Create a Quiz Game
#  Who Painted the Famous artwork "The Starry Night"?
# A Leonardo da Vinci B. Vincent van Gogh C. Pablo Picasso D. Claude Monet  Correct: B
# What is the largest Planet in our solar system?
# A. Earth b. Saturn C. Jupiter D. Uranus  Correct: C
# What does the Acronym "API" stand for in computer?
 # A. Application Proramming Interface B. Artificial Programming Interface C. Advanced Programming Interface D. Automated Programming Interface
#  How many Bones are in the Human Body ?
# A. 206 B. 207 C. 208 D. 209

questions = (
    '1. Who Painted the Famous artwork "The Starry Night"?',
    '2. What is the largest Planet in our solar system?',
    '3. What does the Acronym "API" stand for in computer?',
    '4. How many Bones are in the Human Body ?',
    '5. Which Planet is the Hottest in the Solar System? '
)
options = (
    (
    "A. Leonardo da Vinci ",
    "B. Vincent van Gogh ",
    "C. Pablo Picasso ",
    "D. Claude Monet"
    ),
    (
    "A. Earth ",
    "b. Saturn ",
    "C. Jupiter ",
    "D. Uranus"
    ),
    (
    "A. Application Programming Interface ",
   "B. Artificial Programming Interface ",
   "C. Advanced Programming Interface",
    "D. Automated Programming Interface"
    ),
    (
    "A. 206 ",
    "B. 207 ",
    "C. 208 ",
   "D. 209"
    ),
(
    "A. Jupiter ",
    "B. Mercury ",
    "C. Venus ",
   "D. Mars"
    )
)
Answers = [
    "B", "C", "A", "A", "C"
]
guesses = []
score = 0
itt_index = 0

name = input("Please Enter your name: ").upper()
for question in questions:
    print("------------------------------------------------------")
    print(question)
    for option in options[itt_index]:
        print(option)

    guess = input("Enter Your Answer(A,B,C,D) : ")
    guesses.append(guess)
    if guess.upper() == Answers[itt_index]:
        print("CORRECT")
        score += 1
    else: print(f"INCORRECT \n{Answers[itt_index]} is the Correct Answer")


    itt_index +=1
print("\n")
print("---------------------------------------------")
print("                 SCORE                       ")
print("---------------------------------------------")

print(f" CORRECT ANSWERS : {Answers}")
print(f" YOUR ANSWERS: {guesses}")
T_score = int((score / len(Answers)) * 100)
print(f"{name}, your Total Score is {T_score}%")

