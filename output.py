from statistics import stdev
from typing import Dict


DATA: Dict[str, float] = {
    'Madonna Litta': 32.34,
    'Adorazione dei Magi': 30.91,
    'Vergine delle Rocce': 36.92,
    'Madonna of the Carnation': 35.18,
    'Mona Lisa': 30.97,
    'Saint Jerome': 0.05,
    'Salvador Mundi': 41.24,
    'Lady with an Ermine': 62.42,
    'Sala delle Asse': 29.94,
    'La Belle Ferronnière': 67.74,
    'Ginevra de\' Benci': 38.97,
    'Benois Madonna': 46.55,
}


if __name__ == '__main__':
    for title, percentage in DATA.items():
        print(f'{title}\t{percentage}')

    percents = list(DATA.values())
    avg = round(sum(percents) / len(percents), 2)
    print('Average:', avg)
    print('Standard deviation:', stdev(percents))

