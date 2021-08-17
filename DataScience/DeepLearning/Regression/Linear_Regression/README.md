# 선형회기 ( Linear_Regression )

## [수식이 안보이면 클릭 후 설치](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related)

## 간단 설명

- 가설함수를 생성하고, 실제 데이터에 맞는 Weight 과 Bias를 찾는것이 목적

## 프로세스

1.  `X`를 선언한다.
    - 가상의 X를 선언한다.
1.  `Y`를 선언한다.
    - 가상의 Y를 선언한다.
1.  `Weight를` 선언한다.
    - 실질적으로 구하고자 하는 것이다.
    - 의미하는 것은 `가중치`이다.
1.  `Bias`를 선언한다.
    - 실질적으로 구하고자 하는 것이다.
    - ## 편향을 의미한다.
1.  `Hyperparameter`를 선언한다.
    - W와 B를 구할 떄 사용하는 가설함수이다
      - 예시
        - $w_1*x_1 + ... +w_n*x_n  + b$
1.  `Cost`를 선언한다.
    - Loss함수를 구하는 것 이다.
    - 이 모델이 얼마나 잘 객체를 설명하는것에 대한 것을 수치로 보여준다.
1.  `Optimizer`를 선언한다.
    - 파라미터를 갱신하는 부분이다.
    - 즉 위에 선언한 것을 이용하여 실제 가중치등의 변화를 진행시키는 부분이다.

## 예제

1.