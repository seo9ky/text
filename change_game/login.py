class Login: # 로그인 클래스
    def __init__(self, correct_id, correct_pw, max_attempts):
        self.correct_id = correct_id
        self.correct_pw = correct_pw
        self.max_attempts = max_attempts


    def login(self):
        print()
        for i in range(self.max_attempts):
            print("===== 로그인 =====")
            user_id = input("ID를 입력하세요: ")
            user_pw = input("PASSWORD를 입력하세요: ")

            if user_id == self.correct_id and user_pw == self.correct_pw:
                print("로그인 되었습니다.\n")
                return True
            else:
                print(f"아이디 또는 비밀번호가 틀렸습니다 - {self.max_attempts - i - 1}회 남았습니다.\n")

        print(f"로그인 {self.max_attempts}회 실패로 프로그램을 종료합니다.\n")

        return False