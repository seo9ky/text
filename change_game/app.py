from login import Login
from ranking import Ranking
from game import Game


class App:
    def __init__(self):
        self.login = Login("admin", "1234", 3)
        self.ranking = Ranking()


    def print_menu(self):
        print("===== 메뉴 선택 =====")
        print("1. 게임 시작")
        print("2. 랭킹 보기")
        print("3. 게임 종료")


    def input_menu(self):
        while True:
            try:
                menu = int(input("메뉴를 선택하세요: "))
                return menu
            except ValueError:
                print("숫자만 입력해주세요.\n")


    def run(self):
        if not self.login.login():
            return

        while True:
            self.print_menu()
            menu = self.input_menu()

            if menu == 1:
                game = Game()
                nickname, tries = game.play()
                self.ranking.add_record(nickname, tries)

            elif menu == 2:
                self.ranking.show_ranking()

            elif menu == 3:
                print("\n프로그램을 종료합니다.\n")
                break

            else:
                print("잘못된 메뉴입니다.\n")