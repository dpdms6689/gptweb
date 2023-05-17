import random

def generate_lotto_numbers():
    """1부터 45 사이의 숫자 중 6개를 무작위로 선택하여 리스트로 반환합니다."""
    numbers = random.sample(range(1, 46), 6)
    return numbers

if __name__ == '__main__':
    lotto_numbers = generate_lotto_numbers()
    print("생성된 로또 번호는 다음과 같습니다:")
    print(lotto_numbers)