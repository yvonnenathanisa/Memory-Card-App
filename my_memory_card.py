from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import randint, shuffle

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question("What is the capital city of italy","Rome","Vatican city","Napels","Florance"))
questions_list.append(Question("A 6-digit positive integer which contains digit 8 is divisible by 9. Given all its digits are different, what is the sum of the digits of the least possible value of this integer? ","9","18","27","36"))
questions_list.append(Question("What starts with T, ends with T, and has T in it?","Teapot","Treat","Tavern","Cup"))
questions_list.append(Question("Who is the richest person in the world?","Elon Musk","Jeff Bezos","Larry Page","Kim Jong Un"))
questions_list.append(Question("What is the lightest material on earth?","Graphene Aerogel","Graphene Oxide","Graphene Nanoplatelets","Single-Layer Graphene"))
questions_list.append(Question("What part of the brain controls emotions?","Limbic System","Diencephalon","Slyvian fissure","Cerebrum"))
questions_list.append(Question("What is the largest volcano in the solar system?","Olympus Mons","Red eye","Krakatau","Merapi"))
questions_list.append(Question("Which planet gives off more heat than it receives from the sun?","Uranus","Mars","Mercury","Pluto"))
questions_list.append(Question("How far is the moon from earth?","384400 km","384240 km","1853500 km","38404 km"))
questions_list.append(Question("What is the largest moon in the solar system?","Ganymede","Enceladus","Titan","Hyperion"))

app = QApplication([])

# main_windows.setGeometry(100,100,300,200)
layout = QVBoxLayout()

lb_Question = QLabel("Let x be a positive integer whose prime factors are 5 and 11 only. If x has exactly 6 different positive integer factors, what is the smallest value of x?")
Confirmation = QPushButton("Submit")
RadioGroupBox = QGroupBox("Answer Options")
choise_1 = QRadioButton("275")
choise_2 = QRadioButton("605")
choise_3 = QRadioButton("165")
choise_4 = QRadioButton("110")
RadioGroup = QButtonGroup() 
RadioGroup.addButton(choise_1)
RadioGroup.addButton(choise_2)
RadioGroup.addButton(choise_3)
RadioGroup.addButton(choise_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(choise_1)
layout_ans2.addWidget(choise_2)
layout_ans3.addWidget(choise_3)
layout_ans3.addWidget(choise_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Test Result:")
lb_result = QLabel("Are you sure")
lb_correct = QLabel("Here's the answer:")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_result, alignment=Qt.AlignHCenter,stretch=2)

layoutline1 = QHBoxLayout()
layoutline2 = QHBoxLayout()
layoutline3 = QHBoxLayout()

layoutline1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layoutline2.addWidget(RadioGroupBox)
layoutline2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layoutline3.addStretch(1)
layoutline3.addWidget(Confirmation,stretch = 2)
# layoutline3.addStretch(3)

layout_card = QVBoxLayout()
layout_card.addLayout(layoutline1,stretch=2)
layout_card.addLayout(layoutline2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layoutline3,stretch=1)
layout_card.addStretch(1)
layout_card.addStretch(5)

# layout_ans1.addLayout(layout_ans2)
# layout_ans1.addLayout(layout_ans3)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    Confirmation.setText("Next Question")

def show_correct(res):
    lb_result.setText(res)
    show_result()

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    Confirmation.setText("Answer")
    RadioGroup.setExclusive(False)
    choise_1.setChecked(False)
    choise_2.setChecked(False)
    choise_3.setChecked(False)
    choise_4.setChecked(False)
    RadioGroup.setExclusive

answers = [choise_1,choise_2,choise_3,choise_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_ans)
    show_question()

def check_ans():
    if answers[0].isChecked():
        show_correct("Correct!")
        window.score += 1
        print("Statistics \n-Total question: ", window.total, '\n-Right answers:', window.score)
        print("Rating: ",(window.score/window.total*100),"%")

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect:")
            print("Rating: ",(window.score/window.total*100),"%")

def next_question():
    window.total += 1
    print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window. score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if Confirmation.text() == 'Answer':
        check_ans()
    else:
        next_question()

# Answer = QGroupBox("Test result")
# result = QLabel("Are you correct or not")
# correct = QLabel("The answer will be here!")

# layout_res = QVBoxLayout()
# layout_res.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignRight))
# Answer.setLayout(layout_res)

# layoutline1 = QHBoxLayout()
# layoutline2 = QHBoxLayout()
# layoutline3 = QHBoxLayout()

# layoutline1.addWidget(Quetion, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
# layoutline2.addWidget(Box)
# layoutline2.addWidget(Answer)
# Answer.hide()

# layoutline3.addStretch(1)
# layoutline3.addWidget(Confirmation, stretch = 2)
# layoutline3.addStretch(1)

# layout_card = QVBoxLayout()

# layout_card.addLayout(layoutline1, stretch = 2)
# layout_card.addLayout(layoutline2, stretch = 8)
# layout_card.addStretch(1)
# layout_card.addLayout(layoutline3, stretch = 1)
# layout_card.addStretch(1)
# layout_card.addSpacing(5)

# def show_result():
#     '''show pannel'''
#     Box.hide()
#     Answer.show()
#     Confirmation.setText("Next Question")
    
# def Show_Question():
#     Box.show()
#     Answer.hide()
#     Confirmation.setText('Answer')
#     Box.setExclusive(False)
#     choise_1.setChecked(False)
#     choise_2.setChecked(False)
#     choise_3.setChecked(False)
#     choise_4.setChecked(False)
#     Box.setExclusive(True)

# answers = [choise_1,choise_2,choise_3,choise_4]

# def ask(question,right_ans, wrong1, wrong2, wrong3):
#     shuffle(answers)
#     answers[0].setText(right_ans)
#     answers[1].setText(wrong1)
#     answers[2].setText(wrong2)
#     answers[3].setText(wrong3)
#     Quetion.setText(question)
#     correct.setText(right_ans)
#     show_result()

# def show_correct(res):
#     lb_result.setText(res)
#     show_result()

# def check_ans():
#     if answers[0].isChecked():
#         show_correct("Correct!")
#     else:
#         if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
#             show_correct("Incorrect!")

# windows = QWidget()
# windows.setLayout(layout_card)
# windows.setWindowTitle("Memo Card")
# ask("A 6-digit positive integer which contains digit 8 is divisible by 9. Given all its digits are different, what is the sum of the digits of the least possible value of this integer?", "18", "9", "36", "27")
# Confirmation.clicked.connect(check_ans)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle("Inflagitah")
window.resize(400,200)
Confirmation.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)

window.show()
app.exec()