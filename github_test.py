print("hello world")
print("現在是版本3")
import random
class Player:
  def __init__(self,name):#初始化固定寫法，第一個參數必為self，第二格才是真正輸入的參數
    self.name =name
    self.hp =100
    self.power =10
    self.atk =0
    self.defe= 50
    self.born =1
  def training(self):
    print("我要訓練")
    a=random.randint(1,5)
    self.power=self.power+a
    return self.power

  def attack(self):
    b=random.randint(1,10)
    self.atk=self.power+b
    c=random.random()
    if c<0.2:
      print("爆擊")
      self.atk=self.atk*2
    else:
      print("普通攻擊")




    return self.atk