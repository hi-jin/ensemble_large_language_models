# 가제 : ensemble large language models

### 설명

Topic Classification task에 대해, LLM을 이용한 서비스를 제공하는 api들의 결과를 취합 :arrow_right: 비교


### Task (추가중)

- [ ] Topic Classification (KLUE-ynat) 문제를 api를 이용하여 해결하는 기반 구축
  - [ ] 여러 model에 대해 best prompt 알아내기
    - [x] gpt-3.5-turbo
    - [x] text-davinci-003
    - [ ] vicuna
- [ ] KLUE, GLUE에 모두 적용 테스트


### 해결해야 할 문제

- [x] 대량의 데이터에 대한 결과를 확인하려 할 때 max token limit을 넘는 경우 `openai.error.RateLimitError`를 내며 종료되는데, 이에 대한 대처 방안은?
- [ ] 결국 prompt 여러 종류를 사용해가며 출력한 결과를 합칠 건데, 어떤 prompt를 써야하는지 어떤 기준으로 판단할까?
- [ ] token 사용량을 미리 계산하는 방법을 만들어두면 좋지 않을까?
