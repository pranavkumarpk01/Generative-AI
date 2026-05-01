# 🐍 Python Roadmap for Generative AI

> **Purpose:** This document is a comprehensive, end-to-end guide to learning Python specifically for Generative AI development. Every concept is explained from scratch — what it is, why it matters in the AI world, how it works, and how to use it in real code. Whether you are a complete beginner or someone brushing up before diving into LLMs and APIs, this roadmap gives you a clear, structured path from zero to building real AI-powered tools.

---

## 📌 How to Use This Roadmap

Follow the phases in order. Each phase builds on the previous one. Don't skip ahead — the later AI-specific topics (APIs, data processing, projects) all depend on the fundamentals covered in the early phases. For each concept:

1. Read the explanation carefully.
2. Type out the code example yourself (don't copy-paste).
3. Modify it, break it, experiment with it.
4. Move on only when you feel confident.

---

## 🛠 Phase 1: The Basics

> These are the absolute building blocks of Python. Every program you will ever write — including AI chatbots, document summarizers, and API wrappers — starts here.

---

### 1. Variables & Input/Output

#### What is a Variable?

A **variable** is a named container that stores a value in memory. Think of it like a labelled box — you put something inside it, give it a name, and retrieve it whenever needed. In Python, you don't need to declare a type explicitly; Python figures it out on its own.

```python
name = "Pranav"       # Stores the string "Pranav" in a variable called 'name'
age = 22              # Stores the integer 22
score = 98.5          # Stores a decimal (float) number
is_active = True      # Stores a boolean (True or False)
```

Variable names should be descriptive and use `snake_case` (lowercase words separated by underscores). Avoid single-letter names except in simple loops.

#### What is Output — `print()`?

`print()` is Python's built-in function to display output on the screen (the terminal/console). You can print text, numbers, variables, and even expressions.

```python
name = "Pranav"
print(name)                        # Output: Pranav
print("Hello, " + name)           # Output: Hello, Pranav
print(f"My name is {name}")       # f-string — the modern, preferred way
print("Age:", 22)                  # Output: Age: 22
```

**f-strings** (formatted string literals) are the cleanest way to embed variables inside strings. They were introduced in Python 3.6 and are widely used in AI code for building prompts dynamically.

```python
model = "gpt-4"
tokens = 1500
print(f"Model: {model} | Tokens used: {tokens}")
# Output: Model: gpt-4 | Tokens used: 1500
```

#### What is Input — `input()`?

`input()` pauses the program and waits for the user to type something. Whatever they type is captured as a **string**. This is the foundation of any interactive AI chatbot — the user types a query, your program receives it, processes it, and responds.

```python
user_input = input("Enter your name: ")
print("Hello", user_input)
```

**Important:** `input()` always returns a string. If you ask for a number, you must convert it (covered in the next section).

```python
user_query = input("Ask me anything: ")
# user_query now holds whatever the user typed — ready to be sent to an AI API
print(f"You asked: {user_query}")
```

#### 🤖 Why This Matters for Generative AI

Every AI chatbot loop is fundamentally built on `input()` and `print()`. The user sends a message → your program reads it with `input()` → sends it to an AI model → prints the response with `print()`. Even complex AI applications like ChatGPT reduce to this loop at their core.

---

### 2. Data Types & Type Casting

#### What are Data Types?

Every value in Python has a **data type** — a classification that tells Python what kind of data it is and what operations can be performed on it. The core types you'll use constantly are:

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text / string of characters | `"Hello AI"` |
| `int` | Whole numbers | `42`, `-7`, `0` |
| `float` | Decimal numbers | `3.14`, `99.9` |
| `bool` | True or False values | `True`, `False` |
| `NoneType` | Represents nothing / absence of value | `None` |

```python
name = "Pranav"         # str
age = 22                # int
temperature = 36.6      # float
is_ready = True         # bool
result = None           # NoneType — often used as a default before a value is assigned
```

You can always check the type of any variable using `type()`:

```python
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(is_ready))   # <class 'bool'>
```

#### What is Type Casting?

Type casting (or type conversion) means converting a value from one type to another. This is critical when working with user input or API responses, because they often come as strings that need to be treated as numbers, or vice versa.

```python
# Converting string to integer
num_str = "10"
num_int = int(num_str)        # "10" → 10
print(num_int + 5)            # Output: 15

# Converting string to float
price_str = "99.5"
price_float = float(price_str)  # "99.5" → 99.5
print(price_float * 2)          # Output: 199.0

# Converting number to string
age = 22
age_str = str(age)            # 22 → "22"
print("I am " + age_str + " years old")  # This works now — can't add int to string directly

# Converting to boolean
print(bool(1))    # True
print(bool(0))    # False
print(bool(""))   # False — empty string is falsy
print(bool("hi")) # True — non-empty string is truthy
```

#### Common Pitfall: String + Number

```python
# ❌ This will CRASH
age = 22
print("Age: " + age)       # TypeError: can only concatenate str (not "int") to str

# ✅ Fix with type casting or f-strings
print("Age: " + str(age))  # Works
print(f"Age: {age}")        # Also works — Python handles the conversion automatically
```

#### 🤖 Why This Matters for Generative AI

AI APIs (like OpenAI, Anthropic, Gemini) return responses as JSON — which is mostly made up of strings and numbers. When you get back a token count, you need to treat it as an integer to do math. When you build a prompt, you need everything as a string. Type casting bridges the gap between raw API data and the logic your program needs to run.

```python
api_response = {"tokens_used": "1500", "model": "claude-3"}

tokens = int(api_response["tokens_used"])   # Convert string to int
cost = tokens * 0.002                        # Now you can calculate cost
print(f"Cost for this request: ${cost:.4f}")
```

---

## 🚀 Phase 2: Logic & Control Flow

> Programs don't just run top to bottom. They make decisions, repeat actions, and react to different situations. Control flow is what gives your program intelligence — and it's what powers the decision-making layer in every AI application.

---

### 3. Conditional Statements

#### What are Conditionals?

A **conditional statement** lets your program make a decision. It evaluates a condition (something that is either `True` or `False`) and executes different blocks of code depending on the result. This is the `if / elif / else` structure.

```python
age = 20

if age >= 18:
    print("You are an adult.")    # This block runs if the condition is True
else:
    print("You are a minor.")     # This block runs if the condition is False
```

Python uses **indentation** (4 spaces) to define blocks of code. There are no curly braces like in other languages. Getting indentation wrong is one of the most common beginner errors.

#### `elif` — Multiple Conditions

When you have more than two possible outcomes, use `elif` (short for "else if"):

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Your grade is: {grade}")   # Output: Your grade is: B
```

#### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `name != "Admin"` |
| `>` | Greater than | `score > 90` |
| `<` | Less than | `tokens < 1000` |
| `>=` | Greater than or equal | `age >= 18` |
| `<=` | Less than or equal | `price <= 99.99` |

#### Logical Operators: `and`, `or`, `not`

Combine multiple conditions:

```python
age = 25
has_subscription = True

if age >= 18 and has_subscription:
    print("Access granted.")

if age < 13 or not has_subscription:
    print("Access denied.")
```

#### 🤖 Why This Matters for Generative AI

AI applications are full of decision-making logic. Is the user's message too long? Is the response safe? Should you use a cheaper model or a more powerful one? Should you route the question to a search tool or answer directly?

```python
user_message = input("Your message: ")
token_estimate = len(user_message.split())

if token_estimate > 500:
    print("Message too long. Please shorten your input.")
elif "password" in user_message.lower() or "credit card" in user_message.lower():
    print("Sensitive content detected. Cannot process this request.")
else:
    print(f"Sending to AI model: '{user_message}'")
    # → call your AI API here
```

---

### 4. Loops

#### What are Loops?

A **loop** lets you repeat a block of code multiple times without writing it over and over. Python has two types: `for` loops and `while` loops.

#### `for` Loop — Iterate Over a Sequence

A `for` loop runs once for each item in a sequence (like a list, string, or range of numbers).

```python
# Loop through a range of numbers
for i in range(5):          # range(5) produces: 0, 1, 2, 3, 4
    print(f"Step {i}")

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through characters in a string
for char in "AI":
    print(char)             # Output: A, then I
```

#### `while` Loop — Repeat Until a Condition is False

A `while` loop keeps running as long as its condition is `True`. Be careful — if the condition never becomes `False`, you get an infinite loop.

```python
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1              # count = count + 1 — IMPORTANT: without this, infinite loop!

# Output:
# Count is: 0
# Count is: 1
# Count is: 2
```

#### Loop Control: `break` and `continue`

- `break` — exits the loop immediately
- `continue` — skips the rest of the current iteration and moves to the next

```python
# break example — stop when we find what we're looking for
for num in range(10):
    if num == 5:
        print("Found 5, stopping.")
        break
    print(num)

# continue example — skip even numbers
for num in range(10):
    if num % 2 == 0:
        continue            # Skip even numbers
    print(num)              # Only prints odd numbers: 1, 3, 5, 7, 9
```

#### Nested Loops

Loops inside loops — useful for processing 2D data like tables or matrices.

```python
rows = 3
cols = 3

for i in range(rows):
    for j in range(cols):
        print(f"({i},{j})", end=" ")
    print()     # New line after each row
```

#### 🤖 Why This Matters for Generative AI

Loops power almost every AI workflow. Processing a batch of user queries, tokenizing text word by word, reading through dataset rows, retrying a failed API call — all of these use loops.

```python
# Simulating a multi-turn AI chatbot loop
conversation_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    conversation_history.append({"role": "user", "content": user_input})
    # → send conversation_history to AI API
    ai_response = "This is where the AI response would appear."
    conversation_history.append({"role": "assistant", "content": ai_response})

    print(f"AI: {ai_response}")
```

---

## 📊 Phase 3: Data Structures

> Data structures are containers for organizing and storing data. In AI, your data is everything — prompts, responses, configurations, datasets. Knowing which structure to use and when is a core skill.

---

### 5. Lists & Dictionaries

#### Lists — Ordered, Changeable Collections

A **list** is a collection of items stored in a specific order. Items can be of any type and can be changed after creation (lists are **mutable**).

```python
# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]       # Lists can hold mixed types

# Accessing items by index (starts at 0)
print(fruits[0])        # apple
print(fruits[-1])       # cherry — negative index counts from the end

# Modifying items
fruits[1] = "mango"
print(fruits)           # ['apple', 'mango', 'cherry']

# Adding items
fruits.append("grape")          # Add to end
fruits.insert(1, "blueberry")   # Insert at index 1

# Removing items
fruits.remove("apple")          # Remove by value
popped = fruits.pop()           # Remove and return last item

# Useful list operations
print(len(fruits))              # Number of items
print("mango" in fruits)        # True/False — check membership
fruits.sort()                   # Sort in place
print(sorted(numbers, reverse=True))  # Sort descending without modifying original

# Slicing — get a portion of a list
print(numbers[1:4])             # [2, 3, 4] — items at index 1, 2, 3
print(numbers[:3])              # [1, 2, 3] — first 3 items
print(numbers[2:])              # [3, 4, 5] — from index 2 to end
```

#### List Comprehension — Concise List Creation

A powerful Python feature that lets you build lists in one line:

```python
# Standard way
squares = []
for x in range(6):
    squares.append(x ** 2)

# List comprehension — same result, one line
squares = [x ** 2 for x in range(6)]
print(squares)    # [0, 1, 4, 9, 16, 25]

# With a condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

#### Dictionaries — Key-Value Pairs

A **dictionary** stores data as `key: value` pairs. Think of it like a real dictionary — you look up a word (key) and get its definition (value). Keys must be unique; values can be anything.

```python
# Creating a dictionary
user = {
    "name": "Pranav",
    "role": "Developer",
    "age": 22,
    "skills": ["Python", "AI", "APIs"]
}

# Accessing values
print(user["name"])             # Pranav
print(user.get("age"))          # 22 — .get() is safer, returns None if key missing
print(user.get("email", "N/A")) # N/A — default value if key doesn't exist

# Modifying values
user["role"] = "AI Engineer"

# Adding new key-value pairs
user["city"] = "Mangaluru"

# Removing keys
del user["age"]
removed = user.pop("city")      # Removes and returns the value

# Looping through a dictionary
for key, value in user.items():
    print(f"{key}: {value}")

# Useful methods
print(user.keys())              # All keys
print(user.values())            # All values
print("name" in user)           # True — check if key exists
```

#### Nested Structures

Dictionaries and lists are often combined:

```python
# List of dictionaries — like a table of records
chat_history = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."},
    {"role": "user", "content": "How do I learn it?"},
]

# Access nested data
print(chat_history[0]["content"])   # What is Python?
print(chat_history[1]["role"])      # assistant

# Loop through it
for message in chat_history:
    print(f'{message["role"].upper()}: {message["content"]}')
```

#### 🤖 Why This Matters for Generative AI

Every AI API — OpenAI, Anthropic, Gemini — communicates using JSON, which maps directly to Python dictionaries and lists. The conversation you send to an AI model is a list of dictionaries. The response you get back is a dictionary. Mastering these structures is non-negotiable for AI development.

```python
# This is what you send to an AI API
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain machine learning in simple terms."}
]

# This is what the API returns (simplified)
api_response = {
    "id": "msg_abc123",
    "model": "claude-3",
    "content": [{"type": "text", "text": "Machine learning is..."}],
    "usage": {"input_tokens": 20, "output_tokens": 150}
}

# Extracting data from the response
reply_text = api_response["content"][0]["text"]
tokens_used = api_response["usage"]["input_tokens"] + api_response["usage"]["output_tokens"]
print(f"AI replied: {reply_text}")
print(f"Total tokens: {tokens_used}")
```

---

### 6. Tuples & Sets

#### Tuples — Ordered, Immutable Collections

A **tuple** is like a list, but it **cannot be changed** after creation (it is **immutable**). Use tuples for data that should stay constant — coordinates, config values, return values from functions.

```python
# Creating a tuple
coords = (10, 20)
rgb_color = (255, 128, 0)
model_config = ("gpt-4", 4096, 0.7)    # model name, max tokens, temperature

# Accessing values (same as list — by index)
print(coords[0])        # 10
print(model_config[2])  # 0.7

# Tuple unpacking — assign values to multiple variables at once
model_name, max_tokens, temperature = model_config
print(model_name)       # gpt-4
print(temperature)      # 0.7

# Tuples can be used as dictionary keys (lists cannot)
location_map = {
    (28.6, 77.2): "New Delhi",
    (12.9, 77.5): "Bengaluru"
}

# Check membership
print(10 in coords)     # True
print(len(coords))      # 2

# ❌ Tuples cannot be modified
# coords[0] = 50       # TypeError: 'tuple' object does not support item assignment
```

#### Sets — Unordered Collections of Unique Values

A **set** stores items with no duplicates and no guaranteed order. Sets are perfect for deduplication and fast membership checks.

```python
# Creating a set
unique_nums = {1, 2, 2, 3, 3, 3, 4}
print(unique_nums)          # {1, 2, 3, 4} — duplicates removed automatically

# Adding and removing
unique_nums.add(5)
unique_nums.discard(1)      # Remove without error if not found
print(unique_nums)

# Set operations — great for comparing collections
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a & set_b)        # Intersection: {3, 4} — items in both
print(set_a | set_b)        # Union: {1, 2, 3, 4, 5, 6} — all items
print(set_a - set_b)        # Difference: {1, 2} — in A but not B

# Fast membership check
seen_ids = {"id_001", "id_002", "id_003"}
print("id_002" in seen_ids)     # True — very fast even for large sets
```

#### 🤖 Why This Matters for Generative AI

Tuples are used for fixed AI configurations (model name, temperature, max tokens) that should never be accidentally overwritten. Sets are used to deduplicate tokens, track which documents have already been processed, or filter out stop words before feeding text to an AI model.

```python
# Remove duplicate words before processing
raw_words = ["the", "cat", "sat", "on", "the", "mat", "the"]
unique_words = set(raw_words)
print(unique_words)     # {'the', 'cat', 'sat', 'on', 'mat'} — no duplicates

# Track processed document IDs to avoid re-processing
processed_doc_ids = set()

documents = [{"id": "doc_1", "text": "..."}, {"id": "doc_2", "text": "..."}, {"id": "doc_1", "text": "..."}]

for doc in documents:
    if doc["id"] in processed_doc_ids:
        print(f"Skipping already processed: {doc['id']}")
        continue
    processed_doc_ids.add(doc["id"])
    print(f"Processing: {doc['id']}")
    # → send doc["text"] to AI for embedding/summarization
```

---

## ⚙️ Phase 4: Modular Code & Data

> As your programs grow, you need ways to organize code into reusable chunks, read and write files, and handle unexpected failures gracefully. These concepts are essential for production-grade AI applications.

---

### 7. Functions & Lambda

#### What is a Function?

A **function** is a named, reusable block of code that performs a specific task. Instead of writing the same logic repeatedly, you define it once and call it whenever needed. Functions make code cleaner, easier to test, and easier to maintain.

```python
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Pranav")
print(message)          # Hello, Pranav!

print(greet("Alice"))   # Hello, Alice!
print(greet("Bob"))     # Hello, Bob!
```

#### Parameters, Arguments & Return Values

- **Parameters** — the variable names listed in the function definition
- **Arguments** — the actual values you pass when calling the function
- **Return value** — what the function sends back using the `return` keyword

```python
def add(a, b):              # a and b are parameters
    result = a + b
    return result           # Returns the sum

total = add(3, 7)           # 3 and 7 are arguments
print(total)                # 10
```

#### Default Parameter Values

```python
def generate_prompt(topic, style="formal", length=200):
    return f"Write a {style} explanation of '{topic}' in about {length} words."

print(generate_prompt("machine learning"))
# Write a formal explanation of 'machine learning' in about 200 words.

print(generate_prompt("neural networks", style="simple", length=100))
# Write a simple explanation of 'neural networks' in about 100 words.
```

#### `*args` and `**kwargs` — Flexible Arguments

```python
# *args — accept any number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))      # 15

# **kwargs — accept any number of keyword arguments
def build_api_call(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

build_api_call(model="claude-3", temperature=0.7, max_tokens=1000)
```

#### Lambda Functions — One-Line Anonymous Functions

A **lambda** is a small, throwaway function defined in a single line. Use it when you need a simple function for a short period — often when sorting, filtering, or applying transformations.

```python
# Standard function
def square(x):
    return x * x

# Equivalent lambda
square = lambda x: x * x
print(square(5))        # 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 7))        # 10

# Real use case — sorting a list of dicts by a specific key
responses = [
    {"model": "gpt-3.5", "tokens": 500},
    {"model": "claude-3", "tokens": 250},
    {"model": "gemini", "tokens": 800},
]

sorted_by_tokens = sorted(responses, key=lambda r: r["tokens"])
print(sorted_by_tokens)
# [{'model': 'claude-3', 'tokens': 250}, {'model': 'gpt-3.5', 'tokens': 500}, ...]
```

#### 🤖 Why This Matters for Generative AI

Real AI applications are broken into modular functions: one function to build a prompt, one to call the API, one to parse the response, one to log the output. This separation makes code readable, testable, and reusable across different projects.

```python
def build_prompt(user_question, context=""):
    if context:
        return f"Context:\n{context}\n\nQuestion: {user_question}\nAnswer:"
    return f"Question: {user_question}\nAnswer:"

def call_ai_api(prompt, model="claude-3", max_tokens=500):
    # Simulated API call
    return {"response": f"Answer to: {prompt[:30]}...", "tokens": 120}

def extract_response(api_output):
    return api_output.get("response", "No response received.")

def log_usage(api_output, model):
    tokens = api_output.get("tokens", 0)
    print(f"[LOG] Model: {model} | Tokens used: {tokens}")

# Clean, modular workflow
question = "What is reinforcement learning?"
prompt = build_prompt(question)
raw_output = call_ai_api(prompt)
answer = extract_response(raw_output)
log_usage(raw_output, "claude-3")
print(f"\nAI Answer: {answer}")
```

---

### 8. File Handling

#### What is File Handling?

File handling lets your Python program **read from** and **write to** files on disk. This is crucial for AI applications that need to load datasets, save conversation histories, read documents for summarization, or log outputs.

#### Opening and Reading Files

Python uses the `open()` function with a file path and a **mode**:

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates new file or overwrites existing |
| `"a"` | Append — adds to end of existing file |
| `"r+"` | Read and write |

Always use the `with` statement — it automatically closes the file when the block ends, even if an error occurs.

```python
# Reading an entire file
with open("data.txt", "r") as f:
    content = f.read()          # Read everything as one big string
print(content)

# Reading line by line (memory-efficient for large files)
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())     # .strip() removes trailing newline characters

# Reading all lines into a list
with open("data.txt", "r") as f:
    lines = f.readlines()       # Returns ['line1\n', 'line2\n', ...]
```

#### Writing to Files

```python
# Writing (overwrites existing content)
with open("output.txt", "w") as f:
    f.write("This is the first line.\n")
    f.write("This is the second line.\n")

# Appending (adds to existing content)
with open("output.txt", "a") as f:
    f.write("This line is appended.\n")
```

#### Working with JSON Files

JSON (JavaScript Object Notation) is the standard format for AI API data. Python's `json` module makes reading/writing JSON files seamless.

```python
import json

# Writing a dictionary to a JSON file
conversation = {
    "session_id": "abc123",
    "messages": [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there!"}
    ]
}

with open("conversation.json", "w") as f:
    json.dump(conversation, f, indent=4)    # indent=4 makes it human-readable

# Reading a JSON file back into a dictionary
with open("conversation.json", "r") as f:
    loaded_conversation = json.load(f)

print(loaded_conversation["session_id"])    # abc123
print(loaded_conversation["messages"][0])   # {'role': 'user', 'content': 'Hello'}
```

#### 🤖 Why This Matters for Generative AI

AI document summarizers read `.txt` or `.pdf` files. Chatbots save conversation history to JSON so the context persists between sessions. Training datasets are loaded from `.csv` files. API responses are logged to files for debugging and billing tracking.

```python
import json

def save_conversation(history, filename="chat_history.json"):
    with open(filename, "w") as f:
        json.dump(history, f, indent=2)
    print(f"Conversation saved to {filename}")

def load_conversation(filename="chat_history.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []   # Start fresh if no file exists

# Resume a previous conversation
history = load_conversation()
history.append({"role": "user", "content": "Continue our discussion."})
# → send history to AI API
save_conversation(history)
```

---

### 9. Exception Handling

#### What are Exceptions?

An **exception** is an error that occurs while your program is running. If unhandled, it crashes your program with an error message. **Exception handling** lets you anticipate these errors and respond to them gracefully — showing a friendly message, retrying, or falling back to a default — instead of crashing.

#### `try / except` — The Basic Structure

```python
# Without exception handling — this CRASHES
result = 10 / 0        # ZeroDivisionError: division by zero

# With exception handling — this HANDLES the error
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    result = 0

print(f"Result: {result}")  # Result: 0
```

#### Catching Multiple Exception Types

```python
try:
    user_input = input("Enter a number: ")
    number = int(user_input)        # May raise ValueError
    result = 100 / number           # May raise ZeroDivisionError
    print(f"Result: {result}")

except ValueError:
    print("Invalid input — please enter a numeric value.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    # Catch-all for any other unexpected errors
    print(f"An unexpected error occurred: {e}")
```

#### `else` and `finally`

```python
try:
    num = int("42")
except ValueError:
    print("Conversion failed.")
else:
    # Runs ONLY if no exception occurred
    print(f"Conversion successful: {num}")
finally:
    # ALWAYS runs — whether or not an exception occurred
    print("This always executes — good for cleanup.")
```

#### Common Built-in Exceptions

| Exception | When it occurs |
|-----------|----------------|
| `ValueError` | Wrong value type (e.g., `int("abc")`) |
| `TypeError` | Wrong type for an operation |
| `KeyError` | Accessing a dict key that doesn't exist |
| `IndexError` | Accessing a list index out of range |
| `FileNotFoundError` | Opening a file that doesn't exist |
| `ZeroDivisionError` | Dividing by zero |
| `ConnectionError` | Network/API connection failure |
| `TimeoutError` | Request took too long |

#### 🤖 Why This Matters for Generative AI

AI applications rely on external APIs over the internet. Networks are unreliable. APIs have rate limits, timeouts, and occasional outages. Without exception handling, a single failed API call crashes your entire application. With it, you can retry, log the error, and keep running.

```python
import time

def call_ai_with_retry(prompt, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt}: Calling AI API...")
            # Simulated API call — replace with real API call
            if attempt < 3:
                raise ConnectionError("API temporarily unavailable")
            response = {"text": "Here is the AI response."}
            return response["text"]

        except ConnectionError as e:
            print(f"Connection error: {e}. Retrying in 2 seconds...")
            time.sleep(2)

        except KeyError:
            print("Unexpected API response format.")
            return None

    print("All retries failed.")
    return None

result = call_ai_with_retry("Summarize this document.")
print(f"Final result: {result}")
```

---

## 🧪 Phase 5: The AI Ecosystem

> Now that you have a solid Python foundation, it's time to work with the libraries that power real-world AI and data science. NumPy and Pandas are the bedrock of data processing in every AI pipeline.

---

### 10. NumPy & Pandas

#### NumPy — Numerical Computing

**NumPy** (Numerical Python) provides the `ndarray` — a fast, efficient array object for numerical computation. It is the backbone of almost every scientific computing and machine learning library in Python.

**Install:** `pip install numpy`

```python
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print(arr1)             # [1 2 3 4 5]
print(type(arr1))       # <class 'numpy.ndarray'>

# Array operations — applied element-wise (unlike Python lists)
print(arr1 + arr2)      # [11 22 33 44 55]
print(arr1 * 2)         # [2 4 6 8 10]
print(arr1 ** 2)        # [1 4 9 16 25]

# Statistical functions
print(np.mean(arr1))    # 3.0
print(np.sum(arr1))     # 15
print(np.max(arr1))     # 5
print(np.std(arr1))     # Standard deviation

# 2D arrays (matrices)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.shape)         # (3, 3) — 3 rows, 3 columns
print(matrix[0])            # [1 2 3] — first row
print(matrix[:, 1])         # [2 5 8] — second column
print(matrix[1, 2])         # 6 — row 1, column 2

# Creating special arrays
zeros = np.zeros((3, 3))        # 3x3 matrix of zeros
ones = np.ones((2, 4))          # 2x4 matrix of ones
identity = np.eye(3)            # 3x3 identity matrix
random_arr = np.random.rand(5)  # 5 random floats between 0 and 1
```

#### Pandas — Data Analysis & Manipulation

**Pandas** is built on top of NumPy and provides two core data structures — `Series` (1D) and `DataFrame` (2D table) — for working with structured data like CSV files, spreadsheets, and API responses.

**Install:** `pip install pandas`

```python
import pandas as pd

# Creating a DataFrame — like a spreadsheet table
data = {
    "Prompt": ["What is AI?", "Explain loops", "Summarize this"],
    "Response_Length": [250, 180, 320],
    "Model": ["claude-3", "gpt-4", "claude-3"],
    "Tokens_Used": [300, 220, 400]
}

df = pd.DataFrame(data)
print(df)
#              Prompt  Response_Length     Model  Tokens_Used
# 0       What is AI?              250  claude-3          300
# 1     Explain loops              180     gpt-4          220
# 2  Summarize this               320  claude-3          400

# Basic inspection
print(df.shape)             # (3, 4) — 3 rows, 4 columns
print(df.dtypes)            # Data type of each column
print(df.describe())        # Statistical summary of numeric columns
print(df.head(2))           # First 2 rows
print(df.tail(1))           # Last 1 row

# Accessing data
print(df["Model"])              # Entire 'Model' column (returns a Series)
print(df[["Prompt", "Model"]])  # Multiple columns (returns a DataFrame)
print(df.iloc[0])               # First row by integer index
print(df.loc[1, "Tokens_Used"]) # Row 1, 'Tokens_Used' column → 220

# Filtering rows
claude_rows = df[df["Model"] == "claude-3"]
print(claude_rows)

high_token_rows = df[df["Tokens_Used"] > 250]
print(high_token_rows)

# Adding a new column
df["Cost_USD"] = df["Tokens_Used"] * 0.002
print(df)

# Grouping and aggregation
summary = df.groupby("Model")["Tokens_Used"].mean()
print(summary)
# Model
# claude-3    350.0
# gpt-4       220.0

# Reading from and writing to CSV
df.to_csv("ai_logs.csv", index=False)
loaded_df = pd.read_csv("ai_logs.csv")
print(loaded_df)
```

#### 🤖 Why This Matters for Generative AI

Before you can fine-tune a model, build a RAG (Retrieval Augmented Generation) system, or evaluate AI outputs, you need to handle data — clean it, filter it, aggregate it, and analyze it. Pandas is the standard tool for all of this. NumPy is used under the hood in every vector/embedding operation that powers semantic search and similarity matching.

```python
import pandas as pd

# Load a dataset of AI conversation logs
df = pd.read_csv("conversation_logs.csv")

# Clean up — remove incomplete rows
df.dropna(subset=["user_message", "ai_response"], inplace=True)

# Filter — only keep conversations with helpful ratings
helpful_df = df[df["rating"] >= 4]

# Analyze — average token usage by model
avg_tokens = df.groupby("model")["tokens_used"].mean()
print("Average token usage per model:")
print(avg_tokens)

# Export the clean, filtered dataset for fine-tuning
helpful_df[["user_message", "ai_response"]].to_csv("training_data.csv", index=False)
print(f"Exported {len(helpful_df)} training examples.")
```

---

## 🏗️ Phase 6: Projects

> This is where everything comes together. Each project is designed to use the concepts from the previous phases in a real, end-to-end application. Don't just read these — build them. Modify them. Make them your own.

---

### Project 1: AI Chatbot (using Lists & Loops)

**Concepts used:** Variables, Input/Output, Loops, Lists, Functions, Exception Handling

**What it does:** A terminal-based chatbot that maintains conversation history across multiple turns and simulates an AI response. When connected to a real API (like Anthropic or OpenAI), this becomes a fully functional chatbot.

```python
def get_ai_response(conversation_history):
    """
    Simulated AI response function.
    In production, replace this with a real API call.
    """
    last_user_message = conversation_history[-1]["content"]
    return f"[AI Response to: '{last_user_message[:40]}...']"

def run_chatbot():
    print("=" * 50)
    print("  🤖 AI Chatbot — Type 'quit' to exit")
    print("=" * 50)

    conversation_history = [
        {"role": "system", "content": "You are a helpful and friendly AI assistant."}
    ]

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Please enter a message.")
                continue

            if user_input.lower() in ["quit", "exit", "bye"]:
                print("\nAI: Goodbye! Have a great day! 👋")
                break

            # Add user message to history
            conversation_history.append({
                "role": "user",
                "content": user_input
            })

            # Get AI response
            ai_reply = get_ai_response(conversation_history)

            # Add AI response to history
            conversation_history.append({
                "role": "assistant",
                "content": ai_reply
            })

            print(f"\nAI: {ai_reply}")
            print(f"[Turn {len([m for m in conversation_history if m['role'] == 'user'])}]")

        except KeyboardInterrupt:
            print("\n\nAI: Goodbye!")
            break

run_chatbot()
```

---

### Project 2: Document Summarizer (using File Handling)

**Concepts used:** File Handling, Functions, Exception Handling, String operations, JSON

**What it does:** Reads a text file, breaks it into chunks if it's long, and summarizes each chunk (simulated here — replace with a real API call for actual summarization).

```python
import json
import os
from datetime import datetime

def read_document(filepath):
    """Read and return the content of a text file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Document not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    word_count = len(content.split())
    print(f"📄 Loaded document: {filepath}")
    print(f"   Word count: {word_count}")
    return content

def chunk_text(text, chunk_size=500):
    """Split text into chunks of approximately chunk_size words."""
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

def summarize_chunk(chunk, chunk_num):
    """
    Simulated summarization — replace with real API call.
    Real version: send chunk to AI API, return response text.
    """
    word_count = len(chunk.split())
    return f"[Summary of chunk {chunk_num}: {word_count} words processed. Key ideas extracted.]"

def save_summary(summary_data, output_file="summary_output.json"):
    """Save the full summary results to a JSON file."""
    with open(output_file, "w") as f:
        json.dump(summary_data, f, indent=2)
    print(f"\n✅ Summary saved to: {output_file}")

def summarize_document(filepath):
    try:
        # Step 1: Read the document
        content = read_document(filepath)

        # Step 2: Chunk the text
        chunks = chunk_text(content, chunk_size=300)
        print(f"\n📦 Split into {len(chunks)} chunk(s) for processing.\n")

        # Step 3: Summarize each chunk
        chunk_summaries = []
        for i, chunk in enumerate(chunks, start=1):
            print(f"  Processing chunk {i}/{len(chunks)}...")
            summary = summarize_chunk(chunk, i)
            chunk_summaries.append({"chunk": i, "summary": summary})

        # Step 4: Combine summaries
        full_summary = " ".join([cs["summary"] for cs in chunk_summaries])

        # Step 5: Build output
        output = {
            "source_file": filepath,
            "processed_at": datetime.now().isoformat(),
            "total_chunks": len(chunks),
            "chunk_summaries": chunk_summaries,
            "full_summary": full_summary
        }

        # Step 6: Save output
        save_summary(output)
        print(f"\n📝 Full Summary:\n{full_summary}")

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the summarizer
summarize_document("document.txt")
```

---

### Project 3: Web Scraper (using Libraries)

**Concepts used:** Libraries (`requests`, `BeautifulSoup`), Functions, Lists, Dictionaries, File Handling, Exception Handling

**What it does:** Scrapes a webpage for its headings and paragraphs, then saves the raw text to a file — ready to be fed into an AI API for summarization, Q&A, or analysis.

**Install dependencies:** `pip install requests beautifulsoup4`

```python
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def fetch_page(url):
    """Fetch the HTML content of a webpage."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; AI-Scraper/1.0)"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()     # Raises exception for 4xx/5xx errors
        print(f"✅ Successfully fetched: {url}")
        return response.text

    except requests.exceptions.ConnectionError:
        print("❌ Connection error — check your internet or the URL.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")

    return None

def parse_content(html):
    """Extract headings and paragraphs from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Extract page title
    title = soup.find("title")
    title_text = title.get_text(strip=True) if title else "No title found"

    # Extract all headings
    headings = []
    for tag in ["h1", "h2", "h3"]:
        for heading in soup.find_all(tag):
            text = heading.get_text(strip=True)
            if text:
                headings.append({"level": tag.upper(), "text": text})

    # Extract all paragraphs
    paragraphs = []
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) > 50:              # Skip very short paragraphs
            paragraphs.append(text)

    return {
        "title": title_text,
        "headings": headings,
        "paragraphs": paragraphs,
        "total_paragraphs": len(paragraphs)
    }

def save_for_ai(parsed_data, url, output_file="scraped_content.json"):
    """Save parsed content ready for AI processing."""
    output = {
        "url": url,
        "scraped_at": datetime.now().isoformat(),
        "title": parsed_data["title"],
        "headings": parsed_data["headings"],
        "paragraphs": parsed_data["paragraphs"],
        # Combine all text for easy AI ingestion
        "full_text": "\n\n".join(parsed_data["paragraphs"])
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Saved {parsed_data['total_paragraphs']} paragraphs to {output_file}")
    print(f"   Ready for AI processing!")

def scrape_and_prepare(url):
    print(f"\n🌐 Scraping: {url}\n")

    html = fetch_page(url)
    if not html:
        return

    parsed = parse_content(html)

    print(f"📌 Title: {parsed['title']}")
    print(f"📋 Found {len(parsed['headings'])} headings and {parsed['total_paragraphs']} paragraphs.")

    if parsed["headings"]:
        print("\nHeadings found:")
        for h in parsed["headings"][:5]:    # Show first 5
            print(f"  [{h['level']}] {h['text']}")

    save_for_ai(parsed, url)

# Run the scraper
scrape_and_prepare("https://en.wikipedia.org/wiki/Generative_artificial_intelligence")
```

---

## 💡 Final Advice

### Practice Daily

Consistency beats intensity. One focused hour every day will build stronger skills than a five-hour marathon once a week. Your brain consolidates what it learns while you sleep — daily practice means daily consolidation.

A good daily routine:
- **15 min** — Review yesterday's concept
- **30 min** — Write new code (always type it, never copy-paste)
- **15 min** — Experiment, break things, fix them

### Project-First Learning

Every concept you learn should immediately become a tool you build. Finished learning loops? Build a simple word frequency counter. Learned file handling? Build a log reader. This forces you to think about how concepts apply in real situations, not just in exercises.

Suggested mini-projects per phase:
- **Phase 1** — A personal info card printer
- **Phase 2** — A number guessing game
- **Phase 3** — A contact book (using lists + dicts)
- **Phase 4** — A file-based note-taking app
- **Phase 5** — A CSV data analyzer
- **Phase 6** — Full AI chatbot with memory

### Read the Docs

Get comfortable reading official documentation early. It's a skill in itself. The two you'll use most:

- **Python Docs:** [docs.python.org](https://docs.python.org)
- **Anthropic API Docs:** [docs.anthropic.com](https://docs.anthropic.com)
- **OpenAI API Docs:** [platform.openai.com/docs](https://platform.openai.com/docs)
- **Pandas Docs:** [pandas.pydata.org/docs](https://pandas.pydata.org/docs)

### The AI Builder Mindset

The difference between someone who learns Python and someone who builds AI tools is this: the builder always asks *"How can I apply this to something real?"* Every function, loop, and data structure in this roadmap exists inside every AI system you've ever used. You now have the map — go build.

---

*End of Roadmap — Python for Generative AI*
