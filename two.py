x = 5
print(x)
print(x==5)

x=4
print(x)
print(x==5)
print(x!=5)
print(x > 5)
print(x < 5)
print(x >= 5)
print(x <= 5)
# 一個等號是存入  兩個等號是比較
print("--------------------------我是分隔線----------------------------------------")

answer = input('今天有下雨嗎?')

if answer == 'yes':
   print("我就知道!")

if answer != 'yes':
   print("誠實喔")


print("--------------------------我是分隔線----------------------------------------")

age = input('請輸入年齡?') #input存下來的永遠是字串
age = int(age) #型別轉換

print("--------------------------我是分隔線----------------------------------------")
answer_02 = input('請問要攝氏轉華氏嗎? 是/否')
if answer_02 == '是':
    cel_to_fa = input('請輸入攝氏溫度')
    final_answer = float(cel_to_fa)*9/5+32
    print(final_answer)

if answer_02 != '是':
    fa_to_cel = input('請輸入華氏溫度')
    final_answer = (float(fa_to_cel)-32)*5/9
    print(final_answer)

print("--------------------------我是分隔線----------------------------------------")
