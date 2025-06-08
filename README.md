# Python Basic Quiz Game

A interactive console-based quiz game built in Python to help users practice basic programming concepts. 
This game uses GPT-generated questions to keep the experience dynamic and personalized, with a fallback system for offline or error scenarios.

> 🏁 This is my final project for Stanford University's Code in Place course.

## Features

- **Dynamic question generation** using ChatGPT via `call_gpt()`
- **Fallback question pool** for reliable offline play or API errors. Users can set the questions with JSON file.
- **Instant feedback** using GPT responses (encouragement or fun facts)
- **User-controlled gameplay** — choose how many questions you want
- **Replayable** — play as many times as you'd like

## How It Works

1. The game welcomes you and asks how many questions you want (up to 10).
2. It attempts to generate those questions using GPT via `call_gpt()`.
3. If GPT fails or returns an invalid result, fallback questions are selected randomly.
4. You answer each question interactively and receive AI-generated feedback.
5. At the end, your score is displayed along with a personalized message from GPT.
6. You can choose to play again or exit.

## Requirements

- Python 3.7+
- An implementation of `call_gpt(prompt: str)` in an `ai` module.

> ⚠️ The `call_gpt()` function in the `ai` module is only usable within the **Code in Place console environment**.

## Getting Started

1. Clone or download this repository.
2. Copy the code to **Code in Place console environment**.

## Sample Output of the file
Click here to see it: https://github.com/Jessili8/PythonBasicQuiz/blob/main/quiz_sample_output.md

## Development Experience

Creating this project was a great exercise in combining AI interaction with Python scripting. It involved designing GPT prompts that return structured JSON, handling exception flows gracefully, and ensuring an intuitive user experience through replay options and responsive messaging. The result is a tool that can serve both as a learning exercise and an educational app for Python beginners.

## Future Ideas

- Support for multiple difficulty levels
- Topics beyond Python (e.g., JavaScript, HTML)
- Score tracking and high score leaderboard
- Web-based or GUI version
