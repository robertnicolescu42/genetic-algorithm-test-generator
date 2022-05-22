import random
from questionsList import questions

GD = 7

number_of_questions = len(questions)


def foo(arr):
    answer = 0
    for el in arr:
        answer = el + answer
    return answer - GD


def fitness(arr):
    ans = foo(arr)

    if ans == GD:
        return 99999
    else:
        return abs(1 / ans)


best_found_solution = []
rank = 0

# generare de solutii
solutions = []
for s in range(1000):
    random_tuple = []
    for t in range(GD):
        random_tuple.append(random.uniform(0, 10000))
    solutions.append(random_tuple)

for i in range(10000):
    ranked_solutions = []
    for s in solutions:
        ranked_solutions.append((fitness(s[0], s[1], s[2]), s))
    ranked_solutions.sort(reverse=True)
    print(f'=== Gen. {i} best solutions === ')
    print(ranked_solutions[0])

    if ranked_solutions[0][0] > 999:
        rank, best_found_solution = ranked_solutions[0]
        break

    best_solutions = ranked_solutions[:100]
    elements = []

    for s in best_solutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])

    new_gen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)

        new_gen.append((e1, e2, e3))

    solutions = new_gen

print("")
print(rank)
print(best_found_solution)

question_list = []

# for test_questions in best_found_solution:
#     matching_questions = []
#     for q in questions:
#         if q.weight == round(best_found_solution[0]):
#             matching_questions.append(q)
#     question_list.append(random.choice(matching_questions))

# test_sum = 0
# for q in question_list:
#     print(q.text, end="\n")
#     for answers in q.answers:
#         print(answers)
#     user_answer = input("Raspuns:")
#     if user_answer == q.right_answer:
#         print("Corect!")
#         test_sum = test_sum + 1
#     else:
#         print(f'Gresit! Raspunsul corect era {q.right_answer}')
#
# print(f"Felicitari! Ai reusit sa raspunzi corect la {test_sum} intrebari!")
