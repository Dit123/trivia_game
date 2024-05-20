print("Welcome to trivia game"\n)
print("It is a game where you are to answer some questions and will be socre on the questions")

name = input("Enter your name")
age = input("Enter you age")

print(name)
print(age)

 questions = [
        {
            'question': "What is the capital of France?",
            'options': ["Berlin", "Paris", "London", "Rome"],
            'correct_answer': 2
        },
        {
            'question': "Which planet is known as the Red Planet?",
            'options': ["Mars", "Jupiter", "Venus", "Saturn"],
            'correct_answer': 1
        },
        {
            'question': "What is the largest mammal in the world?",
            'options': ["Elephant", "Blue Whale", "Giraffe", "Gorilla"],
            'correct_answer': 2
        }
    ]

score = 0
random.shuffle(questions)

  if check_answer(user_choice, question_data['correct_answer']):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question_data['correct_answer']}.")

        print(f"Your current score is {score}.\n")

    print(f"Game Over! Your final score is {score} out of {len(questions)}.")
