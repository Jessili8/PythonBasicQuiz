from ai import call_gpt
import time
import random
import json

# Welcome message
def welcome():
    print("\nWelcome to the Python Basic Quiz Game!")
    print("Get ready to test your knowledge and have fun!\n")

# Fallback question set
fallback_questions = [
    {"question": "What is the correct syntax to print 'Hello, World!' in Python?", "answer": "print('Hello, World!')", "hint": "Use the print function with parentheses and quotes around the text."},
    {"question": "Which symbol is used to comment a single line in Python?", "answer": "#", "hint": "It’s a symbol placed at the start of the line to ignore that line during execution."},
    {"question": "What is the correct way to create a variable in Python with the value 5?", "answer": "x = 5", "hint": "Use an equal sign to assign a value to a variable."},
    {"question": "Which data type is used to store text in Python?", "answer": "str", "hint": "It’s short for 'string' and usually enclosed in quotes."},
    {"question": "What will be the output of the expression 2 + 3 * 4?", "answer": "14", "hint": "Remember the order of operations (multiplication before addition)."},
    {"question": "How do you start a function definition in Python?", "answer": "Using the 'def' keyword", "hint": "Function definitions in Python begin with a specific keyword followed by the function name and parentheses."},
    {"question": "Which of the following is a valid list in Python?\nA) {1, 2, 3}\nB) (1, 2, 3)\nC) [1, 2, 3]", "answer": "C) [1, 2, 3]", "hint": "Lists are ordered and mutable collections written with square brackets."},
    {"question": "What does the len() function do in Python?", "answer": "Returns the number of items in an object", "hint": "This function is often used to get the size of strings, lists, or tuples."},
    {"question": "What will be the result of this code: print(type(42))?", "answer": "<class 'int'>", "hint": "The type() function shows the data type of the given value."},
    {"question": "What is the output of: bool(0)?", "answer": "False", "hint": "In Python, zero is considered a 'falsy' value."}
]

# Generate questions using GPT
def generate_questions(topic="Python", level="Basic", num_questions=3):
    print("\nWe are asking GPT for generating questions. Let's wait and see... ")
    prompt = (
        f"Generate {num_questions} quiz questions and answers on the topic of {topic} "
        f"at a {level} level. Respond ONLY with a JSON-formatted list of dictionaries, each having 'question', 'answer', and 'hint' keys."
    )
    response = None
    try:
        response = call_gpt(prompt)
        if not response:
            raise ValueError("GPT returned no response. Using fallback questions.")
        if isinstance(response, str):
            questions = json.loads(response)
        else:
            questions = response
        if not isinstance(questions, list):
            raise ValueError("Expected a list of questions, got something else.")
        return questions
    except Exception as e:
        print("\nError parsing GPT response. Here's what was returned:")
        print(response if response else "<No response received>")
        print("Using fallback Python questions.\n")
        return random.sample(fallback_questions.copy(), min(num_questions, len(fallback_questions)))

# Game loop
def run_quiz():
    topic = "Python"
    level = "Basic"

    try:
        num_questions = int(input(f"Enter number of questions (1 to {len(fallback_questions)}): "))
        if num_questions < 1 or num_questions > len(fallback_questions):
            print("Invalid number. Defaulting to 5 questions.")
            num_questions = 5
    except ValueError:
        print("Invalid input. Defaulting to 5 questions.")
        num_questions = 5

    questions = generate_questions(topic, level, num_questions)

    score = 0
    for idx, q in enumerate(questions):
        input(f"\nPress Enter to see Question {idx + 1}...")
        print(f"\nQuestion {idx + 1}: {q['question']}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == q['answer'].lower():
            print("Correct!")
            feedback = call_gpt(f"Give an encouraging message for answering correctly to: {q['question']}")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {q['answer']}")
            feedback = call_gpt(f"Share a fun fact or hint related to this incorrect answer: {q['question']}")

        print("GPT says:", feedback)
        time.sleep(1)

    print(f"\nQuiz Completed! Your final score is: {score}/{len(questions)}")
    final_feedback = call_gpt(
        f"Give a personalized message for someone who scored {score} out of {len(questions)} on a {level} level quiz about {topic}."
    )
    print("GPT says:", final_feedback)

# Replay option
def main():
    while True:
        welcome()
        run_quiz()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
