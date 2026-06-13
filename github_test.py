import random

# Define Item class first, as it's used by Player's potion method
class Potion_of_poison:
  def __init__ (self,name,poisonous_damage):
    self.name=name
    self.poisonous_damage=poisonous_damage

class Item:
  def __init__(self,name,heal_value):
    self.name=name
    self.heal_value=heal_value

class Player:
  def __init__(self,name):#初始化固定寫法，第一個參數必為self，第二格才是真正輸入的參數
    self.name =name
    self.hp =100
    self.power =10

    self.defe= 20
    self.born =1

  def training(self):
    print("我要訓練")
    a=random.randint(1,5)
    self.power=self.power+a
    return self.power

  def attack(self,otherplayer:"Player"): # 更正 在指定類別時，因為是自訂類別，怕pyython看不懂要加引號
    b=random.randint(1,10)
    atk=self.power+b
    c=random.random()
    if c<0.2:
      print("爆擊")
      atk=atk*2
    else:
      print("普通攻擊")
    otherplayer.hurt(atk,self.name)

    return atk

  def hurt(self,atk:int,name:str):
    d=atk-self.defe
    if d<0:
      print("no reaction")
      return self.hp

    self.hp=self.hp-d

    if self.hp <=0:
      self.born=0
      self.hp=0
      print(self.name+"died")
      #break
    else:

      print(self.name+"受到"+name+"傷害，hp剩"+str(self.hp))

  # Redefined potion method to accept an Item object
  def potion(self, item_to_drink:"Item"):
    if self.hp==100:
      print(f"{self.name} 現在是滿血狀態")
      return self.hp
    if self.hp + item_to_drink.heal_value > 100:
      self.hp=100
    else:
      self.hp=self.hp+item_to_drink.heal_value
    print(f"{self.name} 喝了 {item_to_drink.name}，HP 恢復到 {self.hp}")
    return self.hp
  def poisonous_potion(self,potion:"Potion_of_poison",otherplayer:"Player"):
    otherplayer.power=int(otherplayer.power)//int(potion.poisonous_damage)
    print(f"{otherplayer.name}力量剩{otherplayer.power}")
    return otherplayer.power


p1 =Player("Aaron")#執行初始化，並創建Aaron
p2=Player("DORITOS")


p1.training()
p1.training()
p1.training()
p1.training()
p1.training()
p1.training()
p1.training()
p1.training()
p1.training()
p1.training()


print(p1.power)
p2.training()
print(p2.power)
p1.attack(p2)

print(p2.hp)

# Create Item objects
magic_potion = Item("神奇藥水",10)
super_potion = Item("超級藥水",20)
poison = Potion_of_poison("劇毒藥水",3)

# Correctly call the potion method with an Item object
p2.potion(magic_potion)
print(f"p2 current HP: {p2.hp}")
p2.poisonous_potion(poison,p1)
p1.attack(p2)
print(f"{p2.name}hp剩{p2.hp}")
