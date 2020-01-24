# ロボットシステム学 − 課題2
17C1102　中岡翼
## 概要
[課題1](https://github.com/NakaokaTsubasa/robosys2019_LED)のときに作成したLチカを用いて、キーボードで打った文字のモールス信号を発信するプログラムを作成しました。
## 動画
- URL − https://youtu.be/plbPKslE-Jc
## 使用するもの
- Raspberry Pi 3 Model B+
  - Ubuntu 18.04
- LED
- 抵抗：300[Ω]
## 前処理
[課題1](https://github.com/NakaokaTsubasa/robosys2019_LED)でデバイスファイルを作成する
## 使い方
1. `catkin_ws/src/mypkg`下でリポジトリをクローンしてローカルリポジトリの作成
   ```
   $ git clone https://github.com/NakaokaTsubasa/robosys2019_ROS
   $ cd robosys2019_ROS
   ```
2. 以下を入力
   ```
   $ roscore &
   $ rosrun mypkg keyboard_driver.py
   ```
3. 別ターミナルに以下を入力
   ```
   $ rosrun mypkg Lchika.py &
   $ rostopic echo /keyboard
   ```
4. `rosrun mypkg keyboard_driver.py`を動かしているターミナルを選択した状態で文字を打つと、モールス信号が発信される
## LICENSE
This repository is licensed under the BSD 3-Clause License
