class FlashcardQuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
                "correct_answer": "A"
            },
            {
                "question": "Which programming language is known as the 'language of the web'?",
                "choices": ["A. Python", "B. JavaScript", "C. Java", "D. C++"],
                "correct_answer": "B"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "choices": ["A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Claude Monet"],
                "correct_answer": "A"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
                "correct_answer": "C"
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "choices": ["A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Carbon"],
                "correct_answer": "A"
            }
        ]
        self.score = 0

    def ask_question(self, question_data):
        print(question_data["question"])
        for choice in question_data["choices"]:
            print(choice)
        answer = input("Enter your answer (A, B, C, D): ").upper()

        if answer == question_data["correct_answer"]:
            self.score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {question_data['correct_answer']}.")

    def start_game(self):
        print("Welcome to the Flashcard Quiz Game!\n")
        for question_data in self.questions:
            self.ask_question(question_data)
            print()  # Print a blank line between questions

        print(f"Game Over! Your final score is: {self.score}/{len(self.questions)}")

# Start the game
game = FlashcardQuizGame()
game.start_game()
