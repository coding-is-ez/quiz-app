# Create a quiz app for python using guizero
from guizero import App, Box, TextBox, ListBox, PushButton, ButtonGroup, Text, info

# Functions part
candidate = []

question_and_answers = []

def start():
    global name
    global number
    global candidate
    in_name = name.value
    in_number = number.value
    if in_name != "" and in_number != "":
        candidate.append(in_name)
        candidate.append(in_number)
    else:
        info(title = "Notification", text = "You must enter your name and number!")

count = 1

def read_file():
    global question_and_answers
    global count
    with open("question.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split("|")
            question_and_answers.append(parts)
            list_of_questions.insert(f"Question {count}")

            count += 1

    
    

# GUI part
window = App(title = "Quiz but i made the rules")

contestant_info_txt = Text(window, text = "Contestant info")

contestant_info_box = Box(window, layout = "grid")
name_txt = Text(contestant_info_box, text = "Name: ", grid = [0, 0])
name = TextBox(contestant_info_box, width = 30, grid = [1, 0])
number_txt = Text(contestant_info_box, text = "SBD:  ", grid = [0, 1])
number = TextBox(contestant_info_box, width = 30, grid = [1, 1])

start_btn = PushButton(window, text = "Start", command = start)

quiz_txt = Text(window, text = "Test")

quiz_box = Box(window, layout = "grid")

random_txt = Text(quiz_box, grid = [0, 0], text = "Question: ")
list_of_questions = ListBox(quiz_box, grid = [0, 1])

read_file()

print(question_and_answers)

window.display()
