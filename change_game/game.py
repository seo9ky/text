import random


class Game:
    beverages = [
        {"name": "코카콜라", "price": 1200},
        {"name": "칠성사이다", "price": 1100},
        {"name": "오렌지환타", "price": 1500},
        {"name": "맥심커피", "price": 1300},
        {"name": "삼다수", "price": 800},
        {"name": "포카리스웨트", "price": 1400},
    ]


    def __init__(self):
        self.beverage = random.choice(self.beverages) # 음료수 종류 랜덤 선택
        self.payment = self.make_payment() # 투입금액
        self.change = self.payment - self.beverage["price"] # 거스름돈

        # 거스름돈을 500원과 100원으로만 계산
        self.coin_500 = self.change // 500 # 500원 개수
        self.coin_100 = (self.change % 500) // 100 # 100원 개수

        self.difficulty = None # 게임 난이도
        self.attempts = 0 # 시도 횟수


    def make_payment(self): # 음료수 가격보다 높은 투입금액 만들기 (500원 단위)
        while True:
            payment = random.randint(2, 10) * 500 # 1000원~5000원 사이 랜덤값

            if payment > self.beverage["price"]: # 만약 랜덤값이 음료수 가격보다 높으면 투입금액으로 확정
                return payment


    def input_number(self, message): # 0 이상의 정수만 입력
        while True:
            try:
                number = int(input(message))
                if number < 0:
                    print("0 이상의 숫자를 입력해주세요.\n")
                    continue
                return number
            
            except ValueError:
                print("숫자만 입력해주세요.\n")


    def select_difficulty(self): # 게임 난이도 선택
        while True:
            print("\n===== 난이도 선택 =====")
            print("1. EASY")
            print("2. HARD")

            choice = self.input_number("선택: ")

            if choice == 1:
                self.difficulty = "EASY"
                return
            elif choice == 2:
                self.difficulty = "HARD"
                return
            else:
                print("1 또는 2를 선택해주세요.\n")


    def show_quiz(self): # 자판기 + 문제 출력
        print("\n========== 자판기 ==========") # 자판기 출력
        for number, beverage in enumerate(self.beverages, start=1):
            print(f"{number}. {beverage['name']} - {beverage['price']}원")
        print("============================\n")

        print(f"선택 음료: {self.beverage['name']}") # 문제 출력
        print(f"투입 금액: {self.payment}원")


    def check_answer(self, change, coin_500, coin_100): # 사용자 답이 정답인지 확인
        if change != self.change: # 거스름돈 틀리면
            return False

        if self.difficulty == "HARD": # 하드모드일때는 500원 100원 개수도 문제
            return coin_500 == self.coin_500 and coin_100 == self.coin_100

        return True


    def show_hint(self, change, coin_500, coin_100): # 정답 틀렸을 때 힌트 출력
        if change != self.change: # 거스름돈 틀리면
            if change < self.change:
                print("힌트: 거스름돈 금액을 더 크게 입력하세요.")
            else:
                print("힌트: 거스름돈 금액을 더 작게 입력하세요.")

        if self.difficulty == "HARD": # 하드모드일땐 500원 100원 개수도 고려
            if coin_500 != self.coin_500:
                if coin_500 < self.coin_500:
                    print("힌트: 500원 동전 개수를 더 많이 입력하세요.")
                else:
                    print("힌트: 500원 동전 개수를 더 적게 입력하세요.")

            if coin_100 != self.coin_100:
                if coin_100 < self.coin_100:
                    print("힌트: 100원 동전 개수를 더 많이 입력하세요.")
                else:
                    print("힌트: 100원 동전 개수를 더 적게 입력하세요.")


    def play(self): # 게임 실행
        nickname = input("\n닉네임을 입력하세요: ") # 닉네임 입력

        self.select_difficulty() # 난이도 선택

        self.show_quiz() # 문제 제공

        while True:
            print(f"\n현재 시도 횟수: {self.attempts}회") # 현재 시도 횟수 출력
            change_guess = self.input_number("거스름돈은 얼마인가요? ")

            if self.difficulty == "HARD": # 하드모드일때만 500원 100원 개수 물어봄
                coin_500_guess = self.input_number("500원 동전은 몇 개인가요? ")
                coin_100_guess = self.input_number("100원 동전은 몇 개인가요? ")
            else:
                coin_500_guess = None
                coin_100_guess = None

            self.attempts += 1 # 시도 횟수 +1

            if self.check_answer(change_guess, coin_500_guess, coin_100_guess): # 정답이면
                print("\n정답입니다!")
                print(f"\n거스름돈: {self.change}원")

                if self.difficulty == "HARD": # 하드모드일땐 500원 100원 개수까지 출력
                    print(f"500원: {self.coin_500}개")
                    print(f"100원: {self.coin_100}개")

                print(f"최종 시도 횟수: {self.attempts}회\n") # 최종 시도횟수 출력하고 종료
                break

            print("\n틀렸습니다.\n") # 정답이 아니면 힌트 보여줌
            self.show_hint(change_guess, coin_500_guess, coin_100_guess)

        return nickname, self.attempts # 닉네임, 시도 횟수 반환