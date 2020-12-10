all_class=int(input())
strclass_number=input()
str_price=input()
str_demand_number=input()

class_number = strclass_number.split(',')
price = str_price.split(',')
demand_number = str_demand_number.split(',')
# 字串切割，方便運算 #

final_original_price = 0
# 設原價初始值為0 #

for j in range(all_class):
    original_price = int(price[j]) * int(demand_number[j])
    final_original_price += original_price
    # 用迴圈算出原價 #

a_list = []
# 設一個空清單 #

final_discount_price = 0
# 設最終折扣價初始值為0 #
for w in range(len(class_number)):
    int_class_number = int(class_number[w])
    int_price = int(price[int_class_number - 1])
    # 把清單中的字串轉為整數方便之後運算 #
    possible_least_number = demand_number[int_class_number - 1]
    a_list.append(str(possible_least_number))
    # 先把所有有可能特價商品的需求數量放入清單 #

final_least_number=a_list[0]
for a in range(1,len(a_list)):
    if final_least_number>a_list[a]:
        final_least_number=a_list[a]
# 再從清單中取出最小值作為打折套組件數 #

for i in range(len(class_number)):
    int_class_number = int(class_number[i])
    int_price = int(price[int_class_number - 1])
    if int(final_least_number) == 0:
        final_discount_price += (int(demand_number[int_class_number - 1]) * int_price)
        continue
    # 把清單中的字串轉為整數方便之後運算 #
    discount_number_8=(int(final_least_number) // 5)*5
    discount_price_1=int_price * discount_number_8
    # 算出八折優惠有幾組 #
    discount_number_9=int(final_least_number)-discount_number_8
    discount_price_2=int_price *discount_number_9
    # 可九折優惠得部分 #
    part_price=(int(demand_number[int_class_number - 1])-int(final_least_number))* int_price
    # 剩餘不打折部分 #
    final_discount_price = final_discount_price + (discount_price_1 * 0.8 + discount_price_2 * 0.9 + part_price)

b_list = []
# 預設一個空清單 #

final_remain_price = 0
# 設最終剩餘金額初始值為0 #

for k in range(all_class):
    b_list.append(demand_number[k])
    # 先複製一個需求清單 #
for t in range(len(class_number)):
    b_list[int(class_number[t]) - 1] = 0
    # 將已經在前面用折扣價算過的商品需求數量改為0 #
for u in range(all_class):
    remain_price = int(b_list[u]) * int(price[u])
    final_remain_price += remain_price
    # 計算維持原價的商品的總金額 #

final_all_price = int(final_remain_price + final_discount_price)
# 最終付給店家價格會等於最終剩餘價格（未有折扣）加上最終折扣價 #

gap = final_original_price - final_all_price
# 算出原始價格和最終價格的間距 #

if gap >= 1000:
    print(str(final_all_price) + ',' + str(gap // 1000))
    # 題目所求之招生人數乃差價除以1000的商數 #
else:
    print('So sad. I messed up.')
# 依題意印出答案 #