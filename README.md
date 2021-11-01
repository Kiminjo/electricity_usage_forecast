# Dacon AI프렌즈 시즌 3 '공공 데이터 활용 전력수요 및 SMP 예측 AI 경진대회'

데이콘에서 주최한 smp 예측 대회를 진행하며 작성한 코드입니다.
예측 알고리즘으로는 lightgbm과 Rnn LSTM을 이용하여 예측을 진행하였습니다.

lightgbm은 lightgbm_first_prediction 과 lightgbm_second_prediction에 구현하였고,
Rnn LSTM은 lstm에 구현하였습니다.

lightgbm_first_prediction은 2020년 2월 1일부터 2020년 3월 5일까지의 smp를 예측하고,
lightgbm_second_prediction은 2020년 5월 25일부터 2020년 6월 21일까지의 smp를 예측합니다.

예측 결과는 output 폴더의 submission.csv파일에 저장하였습니다.

예측에는 동기간동안의 온도데이터, 원유가격 데이터를 사용하였습니다.

By : 김인조, 박재한, 오동근
