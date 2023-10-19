# 게임 월드 관리 모듈

# 게임 월드의 표현
# 두개의 layer를 갖는 게임월드로 구현
objects = [ [], [] ]  #이 때 같는 layer를 depth, 깊이로 표현 할 수 있다.

# 월드에 객체를 넣는 함수
def add_object(o, depth=0): #o mean's object
    objects[depth].append(o)

#월드를 업데이트하는, 객체들을 모두 업데이트하는 함
def update():
    for layer in objects:
        for o in layer:
            o.update()

#월드 객체들을 모두 그리기
def rander():
    for layer in objects:
        for o in layer:
            o.draw() # draw와 rander는 같은 의미, 앞에서 draw로 작성하여 draw로 표현


#객체 삭제
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('없는데 왜 지우려는 것인가? 미친거 아니야?')