import pprint

class_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, \
                {'school_class': '4b', 'scores': [3, 2, 5, 5, 4]}, \
                {'school_class': '4c', 'scores': [2, 4, 3, 3, 4]}, \
                {'school_class': '4d', 'scores': [5, 4, 2, 5, 5]}]

pprint.pprint(class_scores)

score_class_accumulator = 0
score_avg_accumulator = 0

for score in (class_scores):
    for item in (score['scores']):
        score_class_accumulator += item
    score_avg_class = score_class_accumulator / len(score.get('scores'))
    score_avg_accumulator += score_avg_class
    score_class_accumulator = 0
    print(f"Клас {score['school_class']} средний балл : {score_avg_class}")

print(f'Средний балл всей школе: {score_avg_accumulator / len(class_scores)}')