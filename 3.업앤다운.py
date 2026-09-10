import random


## 공통 기능
def print_wrong_input():
    print("[WARN] 잘못된 입력입니다")


def input_number(message):
    while True:
        try:
            number = int(input(message))
            return number

        except ValueError:
            print("[WARN] 숫자를 입력해주세요")


class File:
    def save_lines(self, file_name, lines):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))

            if lines:
                file.write("\n")


## 전체 프로그램 관리
class Program: # Program 클래스
    def __init__(self):
        self.lotto = Lotto()
        self.updown = UpDown()


    ## 메인 메뉴
    def print_main_menu(self):
        print("\n======== 메뉴 선택 ========")
        print("1. 모드 선택")
        print("2. 기록 확인")
        print("3. 프로그램 종료")


    def input_main_menu(self):
        self.print_main_menu()

        choice = input_number("메뉴를 선택하세요\n>> ")

        return choice


    def run_main_menu(self):
        while True:
            choice = self.input_main_menu()

            if choice == 1:
                self.run_mode_menu()

            elif choice == 2:
                self.run_storage_menu()

            elif choice == 3:
                self.print_program_exit()
                break

            else:
                print_wrong_input()


    ## 모드 메뉴
    def print_mode_menu(self):
        print("\n======== 모드 선택 ========")
        print("1. 로또번호 추출기")
        print("2. 업앤다운 게임")


    def input_mode_menu(self):
        self.print_mode_menu()

        choice = input_number("모드를 선택하세요 (처음으로: 0)\n>> ")

        return choice


    def run_mode_menu(self):
        while True:
            choice = self.input_mode_menu()

            if choice == 0:
                return

            elif choice == 1:
                self.lotto.run_lotto()

            elif choice == 2:
                self.updown.run_updown()

            else:
                print_wrong_input()


    ## 기록 확인 메뉴
    def print_storage_menu(self):
        print("\n======== 저장소 선택 ========")
        print("1. 로또번호 추출 이력")
        print("2. 업앤다운 게임 랭킹")


    def input_storage_menu(self):
        self.print_storage_menu()

        choice = input_number("저장소를 선택하세요 (처음으로: 0)\n>> ")

        return choice


    def run_storage_menu(self):
        while True:
            choice = self.input_storage_menu()

            if choice == 0:
                return

            elif choice == 1:
                self.lotto.show_lotto_history()
                return

            elif choice == 2:
                self.updown.show_ranking()
                return

            else:
                print_wrong_input()
        
    def print_program_exit(self):
        print("프로그램을 종료합니다\n")


# 로또번호
class Lotto: # Lotto 클래스
    def __init__(self):
        self.lotto_history = []
        self.history_limit = 5
        self.file_storage = File()


    ## 로또 메뉴
    def print_lotto_menu(self):
        print("\n======== 로또번호 추출기 ========")
        print("1. 자동 선택")
        print("2. 수동 선택")


    def input_lotto_menu(self):
        self.print_lotto_menu()

        choice = input_number("추출 방식을 선택하세요 (처음으로: 0)\n>> ")

        return choice


    def run_lotto(self):
        while True:
            choice = self.input_lotto_menu()

            if choice == 0:
                return

            elif choice == 1:
                lotto = self.create_auto_lotto()

            elif choice == 2:
                lotto = self.create_manual_lotto()

            else:
                print_wrong_input()
                continue

            self.print_lotto_result(lotto)
            self.save_lotto_history(lotto)

            return


    ## 로또 자동 추출
    def create_auto_lotto(self):
        lotto = []

        while len(lotto) < 6:
            number = self.create_random_lotto_number()

            if self.is_lotto_number_duplicate(lotto, number):
                continue

            lotto.append(number)

        self.sort_lotto(lotto)

        return lotto


    def create_random_lotto_number(self):
        return random.randint(1, 45)


    def is_lotto_number_duplicate(self, lotto, number):
        return number in lotto


    def sort_lotto(self, lotto):
        lotto.sort()


    ## 로또 수동 추출
    def create_manual_lotto(self):
        lotto = []

        count = self.input_manual_count()

        self.input_lotto_numbers(lotto, count)
        self.fill_remaining_lotto_numbers(lotto)
        self.sort_lotto(lotto)

        return lotto


    def input_manual_count(self):
        while True:
            count = input_number("직접 선택할 번호 개수 (0~6): ")

            if self.is_valid_lotto_count(count):
                return count

            self.print_invalid_lotto_count()


    def is_valid_lotto_count(self, count):
        return 0 <= count <= 6


    def print_invalid_lotto_count(self):
        print("[WARN] 0~6 사이의 개수를 입력하세요")


    def input_lotto_numbers(self, lotto, count):
        while len(lotto) < count:
            number = self.input_lotto_number(lotto)

            if not self.is_valid_lotto_number(number):
                self.print_invalid_lotto_number()
                continue

            if self.is_lotto_number_duplicate(lotto, number):
                self.print_duplicate_lotto_number()
                continue

            lotto.append(number)


    def input_lotto_number(self, lotto):
        number = input_number(f"{len(lotto) + 1}번째 번호 (1~45): ")

        return number


    def is_valid_lotto_number(self, number):
        return 1 <= number <= 45


    def print_invalid_lotto_number(self):
        print("[WARN] 1~45 사이의 번호를 입력하세요")


    def print_duplicate_lotto_number(self):
        print("[WARN] 이미 입력한 번호입니다")


    def fill_remaining_lotto_numbers(self, lotto):
        while len(lotto) < 6:
            number = self.create_random_lotto_number()

            if self.is_lotto_number_duplicate(lotto, number):
                continue

            lotto.append(number)


    ## 로또 결과 / 기록
    def print_lotto_result(self, lotto):
        print("선택 결과:", *lotto)


    def save_lotto_history(self, lotto):
        self.lotto_history.append(lotto)
        self.save_lotto_file()


    def get_lotto_history_lines(self):
        recent_history = self.lotto_history[-self.history_limit:]
        lines = []

        for i, numbers in enumerate(reversed(recent_history), start=1):
            number_text = ""

            for number in numbers:
                number_text += f"{number} "

            lines.append(f"{i}회: {number_text.strip()}")

        return lines


    def save_lotto_file(self):
        self.file_storage.save_lines("lotto.txt", self.get_lotto_history_lines())


    ## 로또 이력
    def show_lotto_history(self):
        self.print_lotto_history_title()

        if self.is_history_empty():
            self.print_empty_history()
            return

        self.print_recent_lotto_history()


    def print_lotto_history_title(self):
        print("\n======== 로또번호 추출 이력 ========")


    def is_history_empty(self):
        return not self.lotto_history


    def print_empty_history(self):
        print("[WARN] 이력이 없습니다")


    def print_recent_lotto_history(self):
        for line in self.get_lotto_history_lines():
            print(line)


# 업앤다운 게임
class UpDown: # UpDown 클래스
    def __init__(self):
        self.ranking = []
        self.ranking_limit = 3
        self.file_storage = File()


    ## 업앤다운 게임
    def run_updown(self):
        while True:
            self.print_updown_title()

            nickname = self.input_nickname()

            if self.is_exit_input(nickname):
                return

            max_number = self.input_difficulty()

            if max_number == 0:
                return

            answer = self.create_updown_answer(max_number)

            self.print_game_start(max_number)

            count = self.play_updown_game(answer)

            self.print_game_result(nickname, count)

            self.save_ranking(nickname, count)

            return


    ## 게임 시작
    def print_updown_title(self):
        print("\n======== 업앤다운 게임 ========")


    def input_nickname(self):
        nickname = input("닉네임을 입력하세요 (처음으로: 0)\n>> ")

        return nickname


    def is_exit_input(self, value):
        return value == "0"


    ## 난이도
    def print_difficulty_menu(self):
        print("\n======== 난이도 선택 ========")
        print("1. 쉬움")
        print("2. 중간")
        print("3. 어려움")


    def input_difficulty(self):
        while True:
            self.print_difficulty_menu()

            mode = input_number("난이도를 선택하세요 (처음으로: 0)\n>> ")

            if mode == 0:
                return 0

            elif mode == 1:
                return 10

            elif mode == 2:
                return 100

            elif mode == 3:
                return 1000

            else:
                print_wrong_input()


    ## 게임 준비
    def create_updown_answer(self, max_number):
        return random.randint(1, max_number)


    def print_game_start(self, max_number):
        print("\n======== 게임 시작 ========")
        print(f"숫자를 맞춰보세요~! (1~{max_number})")


    ## 게임 진행
    def play_updown_game(self, answer):
        count = 0

        while True:
            number = self.input_game_number()

            count += 1

            if self.is_correct_answer(number, answer):
                self.print_correct_answer(number)
                break

            elif self.is_bigger_than_answer(number, answer):
                self.print_lower_hint(number)

            else:
                self.print_higher_hint(number)

        return count


    def input_game_number(self):
        number = input_number(">> ")

        return number


    def is_correct_answer(self, number, answer):
        return number == answer


    def is_bigger_than_answer(self, number, answer):
        return number > answer


    def print_correct_answer(self, number):
        print(f"\n{number} => 정답입니다!!")


    def print_lower_hint(self, number):
        print(f"\n{number}보다 더 작은 수입니다!")


    def print_higher_hint(self, number):
        print(f"\n{number}보다 더 큰 수입니다!")


    def print_game_result(self, nickname, count):
        print(f"{nickname}님의 시도 횟수: {count}")


    def save_ranking(self, nickname, count):
        self.ranking.append({"name": nickname, "count": count})
        self.save_updown_file()


    def get_top_ranking(self):
        ranking = self.ranking.copy()
        self.sort_ranking_by_count(ranking)

        return ranking[:self.ranking_limit]


    def sort_ranking_by_count(self, ranking):
        for last_index in range(len(ranking) - 1, 0, -1):
            for index in range(last_index):
                if ranking[index]["count"] > ranking[index + 1]["count"]:
                    ranking[index], ranking[index + 1] = (
                        ranking[index + 1], ranking[index]
                    )


    def get_ranking_lines(self):
        lines = []

        for i, person in enumerate(self.get_top_ranking(), start=1):
            lines.append(f"{i}등. {person['name']}님의 시도 횟수: {person['count']}")

        return lines


    def save_updown_file(self):
        self.file_storage.save_lines("updown.txt", self.get_ranking_lines())


    def show_ranking(self):
        self.print_ranking_title()

        if self.is_ranking_empty():
            self.print_empty_ranking()
            return

        for line in self.get_ranking_lines():
            print(line)


    def print_ranking_title(self):
        print("\n======== 업앤다운 게임 랭킹 ========")


    def is_ranking_empty(self):
        return not self.ranking


    def print_empty_ranking(self):
        print("[WARN] 랭킹이 없습니다")


def main(): # 메인 함수
    game = Program()
    game.run_main_menu()


## 프로그램 실행
if __name__ == "__main__":
    main()
