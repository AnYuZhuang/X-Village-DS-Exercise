# coding: utf-8

# In[44]:


import requests 
import json
url = 'https://raw.githubusercontent.com/x-village/data-structure-course/master/external_data/ptt_0726_s.json'
datas = requests.get(url)
json_files = datas.json()

list_0 = [] #用來儲存推文數(all)的串列
list_1 = [] #用來儲存 "在json_files裡面,['h_推文總數']不為空值" 的篇數 EX: 如果json_files[i]['h_推文總數'] = {},那麼i不會出現在list_1內
for i in range(len(json_files)): #填充list_0 & list_1
    x = json_files[i]['h_推文總數'] 
    if len(x) != 0:
        list_0.append(x['all'])
        list_1.append(i)
        
index_set = sorted(set(list_0),reverse = True) #index_set是 "已經排序過且不重複的" 推文數

#下面使用兩層 for loop, 第一層是針對要比對的推文數, 第二層是針對 json_files[j]['h_推文總數']['all'] 的值
for i in range(len(index_set)):
    for j in list_1:
        x = json_files[j]['h_推文總數']['all']
        if x == index_set[i]: #註1
            print('推文總數 = %d' % index_set[i] )
            print('內容為:', json_files[j] , sep = '\n')
            print('\n')
            
'''註1: 這邊的比對邏輯是: 我們先把已經排序過的推文數(EX:最大推文數為230)拿出來(這個數字我們先稱為a)，然後再拿出每篇文章(json_files[j])內的推
文數(我們稱之為b)來與a比較，若是b與a相等，我們就把內文與推文數印出來。在這裡 a & b 都是一個變數，會隨著每層loop做改變；其中a的值是透過
第一層for loop(外層)來做變化，而b的值是透過第二層for loop(內層)來做變化'''

