import random
from config import GD, population_size, iterations_size, mutation_size
from questionsList import dataset_list

# GD = 10
questions = dataset_list
number_of_questions = len(questions)


def decizie(arr):
    answer = 0
    for el in arr:
        answer = answer + el
    return answer - GD


best_found_solution = []
rank = 0


def fitness(arr):
    ans = decizie(arr)
    if ans == GD:
        return 99999
    else:
        return abs(1 / ans)


def toTuple(a):
    try:
        return tuple(toTuple(i) for i in a)
    except TypeError:
        return a


def crossover(a, b):
    randomness = random.randint(1, len(a) - 1)
    first_crossover = a[0:randomness] + b[randomness:]
    second_crossover = b[0:randomness] + a[randomness:]
    # print(f'genomes: {a}, {b}')
    # print(f'first_crossover = {first_crossover}\nsecond_crossover =  {second_crossover}')
    # print()
    return first_crossover, second_crossover


def tournament(sol_1, sol_2):
    # print("pop")
    # print(sol_1)
    # print(sol_2)
    if sol_1[0] > sol_2[0]:
        return sol_1
    return sol_2

question_list = []
crossovered_solutions = []

def run():
    question_list = []
    # generare de solutii
    solutions = []
    for s in range(population_size):
        random_tuple = []
        for t in range(GD):
            random_tuple.append(round(random.uniform(0, 10000), 2))
        solutions.append(random_tuple)

    # print(f'normal solution: {solutions[0]}')

    # crossover
    for j in range(0, len(solutions), 2):
        sol_1, sol_2 = crossover(solutions[j], solutions[j + 1])
        crossovered_solutions.append(sol_1)
        crossovered_solutions.append(sol_2)

    for i in range(iterations_size):
        ranked_solutions = []
        for s in solutions:
            ranked_solutions.append((fitness(s), s))

        ranked_solutions.sort(reverse=True, key=lambda tup: tup[0])

        # tournament
        tournament_solutions = []
        for j in range(0, len(ranked_solutions), 2):
            sol_winner = tournament(ranked_solutions[j], ranked_solutions[j + 1])
            tournament_solutions.append(sol_winner)

        ranked_solutions = tournament_solutions
        # print(f'=== Gen. {i} best solutions === ')
        # print(ranked_solutions[0])

        if ranked_solutions[0][0] > 999:
            rank, best_found_solution = ranked_solutions[0]
            break

        best_solutions = ranked_solutions[:100]
        elements = []

        for s in best_solutions:
            # print(f's={s}')
            for el in s[1]:
                elements.append(el)
                # print(f'el={el}')

        # print(f'elements={elements}')

        new_gen = []
        for _ in range(mutation_size):
            tup = []
            for q in range(0, GD - random.randint(0, GD - round(GD / 2))):
                tup.append(random.choice(elements) * random.uniform(0.99, 1.01))
            new_gen.append(toTuple(tup))
            # print(f' totuple {totuple(tup)}')
        # print(f' newgen[0] {new_gen[0]}')
        solutions = new_gen

    print("")
    if(rank):
        print(rank)
    # print(best_found_solution)
    if(solutions and best_found_solution):
        print(f'GD={GD}, sum(solutions)={sum(best_found_solution)}')
    print("")
    # print(ranked_solutions)

    for test_questions in best_found_solution:
        matching_questions = []
        for q in questions:
            if q.weight == round(best_found_solution[0]):
                matching_questions.append(q)
                # intrebarile se pot repeta (fiindca momentan nu exista suficiente intrebari
                # cu grad de dificultate diferit.
                # Pentru a evita aparitia aceiasi intrebari de mai multe ori, se poate apela urmatoarea metoda:
                # questions.remove(q)
        if matching_questions:
            question_list.append(random.choice(matching_questions))
    return question_list

test_sum = 0
question_number = 1
#
# f = open("test.txt", "w", encoding="utf-8")
# for q in question_list:
#     answer_number = 1
#     print(f'{question_number}.{q.text} difficulty: {q.weight}', end="\n")
#     f.write(f'{question_number}.{q.text} difficulty: {q.weight}\n')
#     for answers in q.answers:
#         print(f'{question_number}.{answer_number}: {answers}')
#         f.write(f'{question_number}.{answer_number}: {answers}\n')
#         answer_number += 1
#     f.write("\n")
#
#     question_number += 1
#     user_answer = input("Answer:")
#     if user_answer == q.right_answer or user_answer == q.right_answer.lower():
#         print("Correct!")
#         print("")
#         test_sum = test_sum + 1
#     else:
#         print(f'Wrong! The right answer was {q.right_answer}')
#         print("")
#
#     f.write("Right answer: " + q.right_answer + "\n")
# print(f"Congratulations! You answered {test_sum} questions right!")
