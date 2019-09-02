# AI_tictactoe

<h3>MLP를 이용한 인공지능 틱택토 게임</h3>

<h4>1. Dataset</h4>
<a href="https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame">UCI Tic-Tac-Toe Endgame Data Set</a>

원래의 Dataset에서는 문자를 이용하여 착수, 공백, 승리 여부가 표현되어 있어 학습을 돌리기 적합하지 않았다.

이를 해결하기 위하여 아래의 표와 같은 데이터 전처리 작업을 수행하였다.

<table>
  <tr>
    <td>구분</td>
    <td>player1</td>
    <td>player2</td>
    <td>빈 칸</td>
    <td>player1 승리</td>
    <td>player2 승리</td>
  </tr>
  <tr>
    <td>원래 데이터</td>
    <td>x</td>
    <td>o</td>
    <td>b</td>
    <td>true</td>
    <td>false</td>
  </tr>
  <tr>
    <td>치환 데이터</td>
    <td>-1</td>
    <td>1</td>
    <td>0</td>
    <td>-10</td>
    <td>10</td>
  </tr>
</table>

이후 7:3의 비율로 trainning과 test dataset을 분류하였다.
<br><br>
<h4>2. 학습</h4>
 학습은 MLP(Multi Layer Perceptron)을 이용하여 진행하였다.

MLP란 다층구조를 가지고 있는 신경망을 의미하며 input layer 뿐만이 아니라 중간에 위치한 은닉층에서도 연산을 수행하며 단층 신경망보다 우수한 성능을 보인다.

아래의 표는 학습을 진행한 결과물 표이다.
<table>
  <tr>
    <td>항목</td>
    <td>단층 퍼셉트론</td>
    <td>MLP(2층)</td>
    <td>MLP(2층)</td>
  </tr>
  
  <tr>
    <td>학습 횟수</td>
    <td>1000</td>
    <td>1000</td>
    <td>1000</td>
  </tr>
  
  <tr>
    <td>Optimizer</td>
    <td>Adam</td>
    <td>Adam</td>
    <td>Adam</td>
  </tr>
  
  <tr>
    <td>Learing Rate</td>
    <td>1e-1</td>
    <td>1e-3</td>
    <td>3e-1</td>
  </tr>
  
  <tr>
    <td>Layer</td>
    <td>9</td>
    <td>9 / 27</td>
    <td>9(sigmoid) / 27</td>
  </tr>
  
  <tr>
    <td>정답 수</td>
    <td>283</td>
    <td>285</td>
    <td>286</td>
  </tr>
  
  <tr>
    <td>오답 수</td>
    <td>5</td>
    <td>3</td>
    <td>2</td>
  </tr>
  
  <tr>
    <td>정확도(%)</td>
    <td>98.26</td>
    <td>98.96</td>
    <td>99.03</td>
  </tr>
</table>

학습을 완료한 이후에는 각 신경망 값들을 저장하기 위하여 pickle 모듈을 사용하였다.

이후 완료 된 네트워크를 이용하여 실제 게임에서 테스트하는 과정을 수행하였다.
<br><br>
<h4>3. 실제 테스트</h4>

 테스트의 학습을 마무리한 후 저장했던 pickle 파일에서 데이터를 불러와 진행하였다.
 
 현재 Board에서 돌이 놓여있는 것을 data로 변환한 후 돌을 놓을 수 있는 모든 위치에 대하여 탐색한 후 돌을 놓았을 경우 output 값을 이용하여 최종적으로 돌을 놓을 위치를 결정하였다.
 
 아래의 표를 확인해보자.
 
 <table>
  <tr>
    <td>X</td>
    <td>1</td>
    <td>O</td>
  </tr>
  
  <tr>
    <td>X</td>
    <td>O</td>
    <td>2</td>
  </tr>
  
  <tr>
    <td>3</td>
    <td>4</td>
    <td>O</td>
  </tr>
 </table>
 
 현재 상황에서는 X의 차례이며 돌을 놓을 수 있는 위치는 1, 2, 3, 4번 총 4가지의 경우가 존재한다.
 
 이 때, 돌을 놓을 수 있는 모든 위치에 대하여 돌을 놓았다고 가정을 한 이후 네트워크에서 연산을 수행하며 이 때 X가 이길 수 있는 가장 큰 점수를 가지고 있는 위치에 돌을 착수하는 것으로 AI를 구성하였다.
 
 <br><br>
 <h4>4. 결론</h4>
 
 하지만 학습이 완료 된 데이터를 이용하여 게임을 진행한 결과 아쉽게도 좋은 결과를 보여주지는 못하였다.
 
 정확한 위치에 착수하는 경우가 거의 없었으며 게임이 끝나가는 과정에서도 좋은 수를 두는 모습은 찾기 힘들었다.
 
 이러한 모습에 대하여 이유를 분석해보았다.
 
 <ul>
  <li>데이터의 부족</li> 
  전체 데이터의 갯수는 958개이며 이 중 트레이닝 데이터의 갯수는 약 670개이다. 많은 데이터를 이용하여 학습을 한 것이 아니므로 오버피팅이 일어났을 가능성이 크다고 생각한다.
  <li>데이터의 부적합성</li>
  현재 학습을 진행할 때 사용한 데이터는 완료 된 게임에 대한 데이터이다. 이는 게임이 진행될 때 사용할만한 지표로 쓰기에는 무리가 있을수도 있다고 생각한다.
 </ul>
 
 위의 경우 이외에도 게임을 진행할 때 네트워크를 잘못 계산하도록 설계하였을 가능성도 존재한다.
 
 인공지능을 이용한 첫 프로젝트를 진행한 결과 만족스러운 학습 결과가 나타났지만 실제 적용을 할 때에는 좋은 결과를 얻지 못하였다.
 
 아쉽지만 다음에는 보다 좋은 결과를 낼 수 있도록 노력하겠다.
