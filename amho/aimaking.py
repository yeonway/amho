import csv
import random

# 파일에서 동사와 목적어 목록을 읽어오는 함수
def load_csv_file(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row[0].split(" = ") for row in reader]  # '동사 = 나만의 언어' 형식으로 분리
    return data

# 주어 목록
subjects = {
    "나": "wi",
    "너": "re",
    "그": "ro",
    "우리": "wiwi",
    "너희": "rehi",
    "그들": "rohi"
}

# 예문을 만드는 함수
def generate_example_sentence(verbs, objects):
    # 임의로 동사와 목적어를 선택
    verb, conlang_verb = random.choice(verbs)
    obj, conlang_object = random.choice(objects)

    # 임의로 주어 선택
    subject_korean, subject_conlang = random.choice(list(subjects.items()))

    # 문법에 맞는 예문 생성 (예: 주어 + 동사 + 목적어)
    sentence_korean = f"{subject_korean} {obj}을 {verb}."
    sentence_conlang = f"{subject_conlang} {conlang_verb} {conlang_object}."  # 쉼표 제거

    # (나만의 언어) (원문) 형식으로 반환
    return f"{sentence_conlang} {sentence_korean}"

# 동사와 목적어 목록을 불러오기
verbs = load_csv_file("C:/Users/HOME/Desktop/python/tlfgwp/verbs_translated.csv")
objects = load_csv_file("C:/Users/HOME/Desktop/python/tlfgwp/objects_translated.csv")

# 예문 100개 생성
examples = [generate_example_sentence(verbs, objects) for _ in range(100)]

# 예문을 .csv 파일로 저장
with open("generated_sentences.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["나만의 언어", "원문"])  # 헤더 추가
    for example in examples:
        conlang_sentence, korean_sentence = example.split(" ", 1)  # 나만의 언어와 원문 분리
        writer.writerow([conlang_sentence, korean_sentence])

print("100개의 예문을 'generated_sentences.csv' 파일로 저장했습니다.")
