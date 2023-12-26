import random

def present_question(question):
    print(question['text'])
    for i, choice in enumerate(question['choices'], start=1):
        print(f"{i}. {choice}")

def get_user_answer():
    while True:
        try:
            user_input = int(input("Your answer: "))
            return user_input
        except ValueError:
            print("Please enter a valid number.")

def evaluate_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def present_feedback(is_correct):
    if is_correct:
        print("Correct! Great job!")
    else:
        print("Incorrect. Try again next time.")

def main():
    questions = [
        {
            'text': 'What is the capital of France?',
            'choices': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'correct_answer': 3
        },
        {
            'text': 'Which planet is known as the Red Planet?',
            'choices': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
            'correct_answer': 1
        },
        # Add more questions as needed
    ]

    random.shuffle(questions)  # Shuffle the order of questions

    for question in questions:
        present_question(question)
        user_answer = get_user_answer()
        is_correct = evaluate_answer(user_answer, question['correct_answer'])
        present_feedback(is_correct)

if __name__ == "__main__":
    main()
