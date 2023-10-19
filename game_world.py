# 게임 월드 관리 모듈

# 게임 월드의 표현
objects = []

# 월드에 객체를 넣는 함수
def add(o): #o mean's object
    objects.append(o)

#월드를 업데이트하는, 객체들을 모두 업데이트하는 함
def update():
    for o in objects:
        o.update()

#월드 객체들을 모두 그리기
def rander():
    for o in objects:
        o.draw() # draw와 rander는 같은 의미, 앞에서 draw로 작성하여 draw로 표현