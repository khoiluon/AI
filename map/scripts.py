import collections
import math
from collections import defaultdict
from typing import Set
from collections import Counter


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_alphabetically_first_word(text: str) -> str:
    return min(text.split()) if text.strip() else ''

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def sparse_vector_dot_product(v1: collections.defaultdict, v2: collections.defaultdict) -> float:
    dot = 0.0
    for key in v1:
        if key in v2:
            dot += v1[key] * v2[key]
    return dot

def increment_sparse_vector(v1: collections.defaultdict,scale: float, v2: collections.defaultdict) -> None:
    for key in v2:
        v1[key] += scale * v2[key]

def find_nonsingleton_words(text: str) -> Set[str]:
    words = text.split()
    count = Counter(words)
    return {word for word in count if count[word] > 1}


if __name__ == '__main__':
    text = input('Input: ')
    print('Output:' + find_alphabetically_first_word(text))

    point1 = (1, 1)
    point2 = (4, 5)

    v1 = collections.defaultdict(float, {'a': 5, 'b': 7})
    v2 = collections.defaultdict(float, {'a': 2, 'b': 4, 'c': 3})

    print('Khoang cach giua 2 diem %.2f' % euclidean_distance(point1, point2))
    print('Khoang cach giua 2 diem theo phuong vuong goc %.2f' % manhattan_distance(point1, point2))

    print('Tich vo huong: %.2f' % sparse_vector_dot_product(v1, v2))

    increment_sparse_vector(v1, 1.5, v2)
    print('Scale vector:', dict(v1))

    print('Cat chuoi khoang trang:', find_nonsingleton_words(text))

