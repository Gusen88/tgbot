with open('questions.txt', 'r', encoding='utf-8') as f:
    file = f.read().split('\n')
questions = []
answers = []
right_answer = []
right_answers = 0
numbers = []
a = 0
count = 1
for i in range(0, len(file)):
    if i%3 == 0:
        questions.append(file[i])
        numbers.append(a)
        a +=1
    else:
        if i%3 == 1:
            answers.append(file[i])
        else:
            right_answer.append(file[i])