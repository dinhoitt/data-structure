class Browser:
    def __init__(self, homepage: str):
        self.current_page = homepage # 현재 페이지를 홈페이지로 설정
        self.back_history = [] # 이전 페이지 방문 기록 리스트
        self.forward_history = [] # 다음 페이지 방문 기록 리스트

    def visit(self, url):
        if self.current_page:  # 현재 페이지가 존재하면
            self.back_history.append(self.current_page) # 기존 현재 페이지를 이전 페이지 기록에 추가
        self.current_page = url # 새로운 페이지로 현재 페이지 변경
        self.forward_history.clear()  # 새로운 페이지를 방문하면 앞으로 가기 리스트 초기화

    def back(self, steps) -> str: 
        while steps > 0 and self.back_history: # 뒤로 갈 단계가 남아있고 이전 페이지 리스트가 있으면,
            self.forward_history.append(self.current_page) # 현재 페이지를 앞으로 가기 리스트에 추가
            self.current_page = self.back_history.pop() # 현재 페이지를 가장 최근의 이전 페이지로 설정
            steps -= 1 # 한 단계 뒤로 갔으므로 단계 수 감소
        return self.current_page # 최종적으로 도달한 페이지 반환

    def forward(self, steps) -> str:
        while steps > 0 and self.forward_history: # 앞으로 갈 단계가 남아있고 앞으로 가기 리스트가 있으면,
            self.back_history.append(self.current_page) # 현재 페이지를 이전 페이지 리스트에 추가
            self.current_page = self.forward_history.pop() # 현재 페이지를 가장 최근의 다음 페이지로 설정
            steps -= 1 # 한 단계 앞으로 갔으므로 단계 수 감소
        return self.current_page # 최종적으로 도달한 페이지 반환

# 예시 구현
b = Browser("www.kw.ac.kr")
b.visit("klas.kw.ac.kr")
b.visit("youtube.com")
b.visit("instagram.com")
print(b.back(1))  # youtube.com
print(b.back(1))  # klas.kw.ac.kr
print(b.forward(1))  # youtube.com
b.visit("elcomm.kw.ac.kr")
print(b.forward(5))  # elcomm.kw.ac.kr
print(b.back(2))  # klas.kw.ac.kr
print(b.back(10))  # www.kw.ac.kr