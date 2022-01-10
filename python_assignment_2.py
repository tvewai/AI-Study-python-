class Calculator:
    """
    Description:
    해당 클래스는 공학용 계산기를 위한 클래스 입니다.
    해당 클래스는 apple 내장 계산기와 같은 순서로 작동하도록 설계 되어 있습니다.
    record 기능이 있어 과거의 연산 작동 기록들을 확인할 수 있습니다.

    구현된 기능
    1. 사용자로부터 input 변수에 string 타입으로 값을 입력 받습니다.
    2. 입력 받은 string 값을 split_input 변수에 띄워쓰기 단위를 기준으로 split 합니다.
    3. split_input[0]과 split_input[2]는 int 형태로 바꾸어줍니다.
    4. split_input[0]과 split_input[2]를 split_input[1]을 토대로 연산합니다.
    5. 입력된 값들과 그것을 통해 연산된 값을 사용자가 볼 수 있도록 출력합니다. (출력 파트 description 추가)

    example)
    1. 사용자가 '10 + 5'를 입력하고 enter를 누른다.
    2. 입력 받은 '10 + 5'를 연산을 한다.
    3. '10 + 5 = 15' 라는 값을 출력한다.
    """

    # constructor(=생성자), instance 을 생성할때 가장 먼저 실행 되는 함수.
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self, first, second):
        print(self.first + self.second)
        return self.first + self.second

    def sub(self, first, second):
        print(self.first - self.second)
        return self.first - self.second

    def mul(self, first, second):
        print(self.first * self.second)
        return self.first * self.second

    def div(self, first, second):
        print(self.first / self.second)
        return self.first / self.second

"""
Description:
이전의 결과 값이 없을 때인 처음의 상태는 result = None인 형태로 
사용자로부터 첫 번째 값과 연산부호, 두 번째 값, 총 3개의 input을 받아오게 됩니다.
result가 연산에 의해 값이 생겼을 때는 사용자로부터 연산부호와 숫자 두 가지 input 값만 받아오게 됩니다.
"""

result = None
print("숫자와 연산을 입력하세요. ex) 10 + 5 ")

while True:
    if result == None:
        inputs = input()
        split_input = inputs.split(" ")

        '''
        result = None일 때, 
        split_input[0] = first number
        split_input[1] = 연산 부호 
        split_input[2] = second number
        '''
        split_input_0 = int(split_input[0])
        split_input_2 = int(split_input[2])
        calculation = Calculator(split_input_0, split_input_2)

        if split_input[1] == '+':
            result = calculation.sum(split_input_0, split_input_2)
        elif split_input[1] == '-':
            result = calculation.sub(split_input_0, split_input_2)
        elif split_input[1] == '*':
            result = calculation.mul(split_input_0, split_input_2)
        elif split_input[1] == '/':
            result = calculation.div(split_input_0, split_input_2)

    else:
        inputs = input()
        split_input = inputs.split(" ")

        '''
        result = None일 때, 
        split_input[0] = 연산 부호
        split_input[1] = second number
        여기서 first number은 result 변수로, 이전에 연산을 통해 계산되었던 값입니다. 
        '''
        split_input_1 = int(split_input[1])
        calculation = Calculator(result, split_input_1)

        if split_input[0] == '+':
            result = calculation.sum(result, split_input_1)
        elif split_input[0] == '-':
            result = calculation.sub(result, split_input_1)
        elif split_input[0] == '*':
            result = calculation.mul(result, split_input_1)
        elif split_input[0] == '/':
            result = calculation.div(result, split_input_1)

    # 무한루프 종료 시, q
    if inputs == 'q':
        break