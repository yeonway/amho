import random
import string
import csv

# 랜덤 알파벳 3~5개 생성 함수 (중복 없이)
def generate_random_string():
    # 알파벳을 중복 없이 랜덤으로 선택
    length = random.randint(3, 5)
    return ''.join(random.sample(string.ascii_lowercase, length))

# 파일에서 목록 읽기 (동사 또는 목적어)
def load_list_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        items = file.read().splitlines()  # 각 줄을 읽어서 리스트로 반환
    return items

# 동사 목록을 .csv 파일로 저장하는 함수
def save_verbs_to_csv(verbs, output_filename):
    with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for verb in verbs:
            conlang_verb = generate_random_string()  # 동사에 대응되는 랜덤 알파벳 생성
            writer.writerow([f"{verb} = {conlang_verb}"])

# 목적어 목록을 .csv 파일로 저장하는 함수
def save_objects_to_csv(objects, output_filename):
    with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for obj in objects:
            conlang_object = generate_random_string()  # 목적어에 대응되는 랜덤 알파벳 생성
            writer.writerow([f"{obj} = {conlang_object}"])

# 파일 경로 설정 (백슬래시 대신 슬래시 또는 이중 백슬래시 사용)
verb_filename = "C:/Users/HOME/Desktop/python/amho/kor_verbs.txt"  # 동사 목록이 담긴 .txt 파일 경로
object_filename = "C:/Users/HOME/Desktop/python/amho/objects.txt"  # 목적어 목록이 담긴 .txt 파일 경로
verb_output_filename = "verbs_translated.csv"  # 동사에 대한 .csv 파일 경로
object_output_filename = "objects_translated.csv"  # 목적어에 대한 .csv 파일 경로

# 동사와 목적어 목록을 불러오기
verbs = load_list_from_file(verb_filename)
objects = load_list_from_file(object_filename)

# 동사와 목적어를 각각 .csv 파일로 저장
save_verbs_to_csv(verbs, verb_output_filename)
save_objects_to_csv(objects, object_output_filename)

print(f"{verb_output_filename} 파일과 {object_output_filename} 파일이 생성되었습니다.")
