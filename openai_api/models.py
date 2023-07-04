from enum import Enum


class Model(Enum):
    """
    OpenAI API의 모델을 나타내는 Enum 클래스입니다.
    """
    GPT3_5 = 'gpt-3.5-turbo'
    DAVINCI = 'text-davinci-003'
