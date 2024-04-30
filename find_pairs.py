import numpy as np
import itertools

##Подсчет растояния между парой векторов
def calculate_distance(vector1, vector2, p):
    distance = np.linalg.norm(vector1 - vector2, ord=p)
    print(distance)
    return distance

##Находит самые близкие вектора
def find_closest_pairs(vectors, p):
    min_distance = float('inf')
    closest_pairs = []

    for pair in itertools.combinations(enumerate(vectors), 2):
        index1, vector1 = pair[0]
        index2, vector2 = pair[1]
        distance = calculate_distance(vector1, vector2, p)
        
        if distance < min_distance:
            min_distance = distance
            closest_pairs = [(index1, index2)]
        elif distance == min_distance:
            closest_pairs.append((index1, index2))
    return closest_pairs

##Считает вектора из входного файла
def read_vectors(filename):
    with open(filename, 'r') as file:
        k, n = map(int, file.readline().split())
        vectors = [np.array(list(map(float, file.readline().split()))) for _ in range(k)]
    return vectors

##Записывает найденые пары в выхоной файл
def write_closest_pairs(filename, closest_pairs):
    with open(filename, 'w') as file:
        for pair in closest_pairs:
            file.write(f"{pair[0]} {pair[1]}\n")

def main(input_filename, p):
    vectors = read_vectors(input_filename)
    closest_pairs = find_closest_pairs(vectors, p)
    output_filename = f"{input_filename.split('.')}_{p}.txt"
    write_closest_pairs(output_filename, closest_pairs)

if __name__ == "__main__":
    input_filename = input("Введите имя входного файла: ")
    p = float(input("Введите значение параметра p: "))
    main(input_filename, p)
