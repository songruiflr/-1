#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����
���ڣ�2021.11.26
"""

import random
comp_number=random.randint(0,4)

def name_to_number(name):
    if name=="ʯͷ":
        return 0
    if name=="ʷ����":
        return 1
    if name=="ֽ":
        return 2
    if name=="����":
        return 3
    if name=="����":
        return 4

def number_to_name(number):

    if number==0:
        return "ʯͷ"
    if number==1:
        return "ʷ����"
    if number==2:
        return"ֽ"
    if number==3:
        return "����"
    if number==4:
        return "����"

def rpsls(player_choice):
    while player_choice=="����" or player_choice=="ʯͷ" or player_choice=="ֽ" or player_choice=="����" or player_choice=="ʷ����":
        if name_to_number(player_choice)-comp_number==2 or  name_to_number(player_choice)-comp_number==1 or  name_to_number(player_choice)-comp_number==-3 or  name_to_number(player_choice)-comp_number==-4:
         return "��Ӯ��"
        if name_to_number(player_choice)-comp_number==-2 or  name_to_number(player_choice)-comp_number==-1 or  name_to_number(player_choice)-comp_number==3 or name_to_number(player_choice)-comp_number==4:
         return "�����Ӯ��"
        if name_to_number(player_choice)-comp_number==0:
         return "���ͼ��������һ����"
    while player_choice!="����" or player_choice!="ʯͷ" or player_choice!="ֽ" or player_choice=="����" or player_choice!="ʷ����":
         return "Error:No Correct Name"
         break


print("��ӭʹ��RPSLS��Ϸ")
print("����������ѡ��:")
choice_name=input()

result1=number_to_name(comp_number)

print("----------------")
print("����ѡ��Ϊ:%s"%choice_name)
print("�������ѡ��Ϊ:%s"%result1)
result2=rpsls(choice_name)
print("%s"%result2)