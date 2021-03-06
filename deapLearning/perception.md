퍼셉트론
=======

#### 1.정의
- 프랑크 로젠블라크가 고안한 알고리즘.
- 신경망의 기원.
- 입력 x1, x2 출력 y가 있다고 가정하자. 이때 각각의에 w1, w2의 가중치를 적용한 결과의 합이 출력이라고 하면 아래와 같이 정리가 가능하다.
$$
    y = w1x1 + w2x2
$$
- 퍼셉트론은 통과 혹은 막힘 두 가지의 값만 가질 수 있다. 우리는 이를 1과 0으로 정의할 수 있다. 또한 y의 결과가 특정 값 b 이상일 때 통과, 아닐때 막힘으로 정의할 수 있다. 따라서 위의 수식은 아래와 같이 정리할 수 있다.
$$
    y = 0 (w1x1 + w2x2 <= b)
    y = 1 (w1x1 + w2x2 >  b)
$$
- 즉, 우리는 w1, w2, b를 정의함에 따라서 입력 x1, x2에 대해서 분류가 가능하다.
- 단, 수식에서 볼 수 있듯이 퍼셉트론은 선형 그래프를 그리기 때문에 비션형 분류는 불가능 하다. 그러나 이는 퍼셉트론을 여러 개층으로 적용함으로써 해결할 수 있다.

