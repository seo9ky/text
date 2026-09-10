class Ranking:
    def __init__(self):
        self.records = []


    def add_record(self, nickname, tries):
        record = {
            "닉네임": nickname,
            "시도횟수": tries
        }

        self.records.append(record)


    def show_ranking(self):
        if len(self.records) == 0:
            print("등록된 기록이 없습니다.\n")
            return

        # 시도 횟수가 적은 순서대로 정렬
        for i in range(len(self.records)):
            for j in range(i + 1, len(self.records)):
                if self.records[i]["시도횟수"] > self.records[j]["시도횟수"]:
                    temp = self.records[i]
                    self.records[i] = self.records[j]
                    self.records[j] = temp

        print("\n===== 명예의 전당 =====")

        for i in range(min(3, len(self.records))):
            print(f"{i + 1}위 {self.records[i]['닉네임']} {self.records[i]['시도횟수']}회")

        print()