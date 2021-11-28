#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：宋睿
日期：2021.11.26
"""

import random
comp_number=random.randint(0,4)

def name_to_number(name):
    if name=="石头":
        return 0
    if name=="史波克":
        return 1
    if name=="纸":
        return 2
    if name=="蜥蜴":
        return 3
    if name=="剪刀":
        return 4

def number_to_name(number):

    if number==0:
        return "石头"
    if number==1:
        return "史波克"
    if number==2:
        return"纸"
    if number==3:
        return "蜥蜴"
    if number==4:
        return "剪刀"

def rpsls(player_choice):
    while player_choice=="蜥蜴" or player_choice=="石头" or player_choice=="纸" or player_choice=="剪刀" or player_choice=="史波克":
        if name_to_number(player_choice)-comp_number==2 or  name_to_number(player_choice)-comp_number==1 or  name_to_number(player_choice)-comp_number==-3 or  name_to_number(player_choice)-comp_number==-4:
         return "您赢了"
        if name_to_number(player_choice)-comp_number==-2 or  name_to_number(player_choice)-comp_number==-1 or  name_to_number(player_choice)-comp_number==3 or name_to_number(player_choice)-comp_number==4:
         return "计算机赢了"
        if name_to_number(player_choice)-comp_number==0:
         return "您和计算机出的一样呢"
    while player_choice!="蜥蜴" or player_choice!="石头" or player_choice!="纸" or player_choice=="剪刀" or player_choice!="史波克":
         return "Error:No Correct Name"
         break


print("欢迎使用RPSLS游戏")
print("请输入您的选择:")
choice_name=input()

result1=number_to_name(comp_number)

print("----------------")
print("您的选择为:%s"%choice_name)
print("计算机的选择为:%s"%result1)
result2=rpsls(choice_name)
print("%s"%result2)