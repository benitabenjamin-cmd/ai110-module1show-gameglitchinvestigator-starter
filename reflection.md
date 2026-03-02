# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
It was saying the wrong hints. It is not letting me play a new game unless refreshed. The secret number has issues. It should only validate a number between 1 and 100.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I use copilot to fix the errors and to understand the logic. I also use ChatGPT to understand few of the steps and to double check the logic.
AI was correct in helping me understand how to validate and check only number between the range should be entered. I verified using the testcase and also by testing it in the game.
AI suggestion for the testcases was giving me erros because of tuple errors in returning for a function. I verifed by testing and understanding what the compiler error was.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I tested using the testcases and also manually playing around. 
I checked if the range validate between the said numbers and if the entered is a number not a string. It should my code is working. 
Yes I had tuple returning errors and the AI helped me tp redesign those tests to return the correct parameters.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---
The secret number kept changing in the original app everytime a user interacted with the game. So for every interactiob the secret number kept changing. 
Streamlit reruns the script whenever a user interacts with a something like a button or input.
Stored the secret number in a session state and only updated it when starting a new game or changing difficulty level.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


One habit I want to reuse in future is my debugging strategy and testing. 
I would try to first input my idea before the AI passes its idea to me next time.
This project changed my thinking about how AI can give different solutions for things that can have advantages and disadvantages. 
