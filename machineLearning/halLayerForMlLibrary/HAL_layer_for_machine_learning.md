HAL layer for machine learning
==============================

#### 1. HAL API Layer의 의의
|Architecture for machine learning|
|--|
|App|
|Machine learning library(TensorFlow, Caffe..)|
|**HAL API**|
|H/W(GPU, CPU, TPU)|

- Machine learning은 연산량이 많기 때문에 H/W 가속이 필수
- Library에게 있어서 H/W 가속은 반드시 고려해야 하는 요소이자 Library가 얼마나 잘 만들어 졌는지 보여주는 지표
- Library를 잘못 설계하면 H/W에 종속될 가능성이 있음

-> 따라서 HAL API Layer를 잘 구성해야 한다.

#### 2. HAL API의 종류
- Initialize, 모델 생성, 모델 실행, Finalize의 단계로 구분 가능

###### 2.1 Initialize
- 해당 soc에서 지원 가능한 H/W 및 기능 전달
- 사용할 기능에 맞게 파라미터 설정 및 디바이스 초기화

###### 2.2 모델 생성
- CNN등의 사용할 모델 결정
- 모델에 대한 파라미터 설정

###### 2.3 모델 실행
- 2.2에서 섫정한 모델을 실행함
- 중간에 변경해야 하는 파아미터 등을 조정함

###### 2.4 Finalize
- 디바이스에 완료 처리
- 메모리 해제 등

-> 실제 모델에 대한 처리는 ML library 상에서 처리되겠지만 모델에 따라서 특정 연산이 HAL에 정의되고 사용될 것으로 예상이 됨

