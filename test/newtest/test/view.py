from django.shortcuts import render
from django.views.generic import ListView

from .form import TestForm
import ast


def fibo(n, a1=1, a2=0):
  if n < 1:
    return a1
  return fibo(n - 1, a1 + a2, a1)


def dicSearch(strA, dicB, list):
  print('★★')
  templist = []
  substr = strA[:]
  num = 0
  for str in dicB:
    num += 1
    # print('str', str)
    if substr.find(str) >= 0:
      substr = substr.replace(str, "", 1)
      subdic = dicB[num:]
      if substr == '':
        break
      if len(subdic) == 0:
        break

      print(substr)
      print(subdic)
      print(templist)
      dic_search(substr, subdic, templist)
      print('subsub', templist)
      if len(templist) > 0:
        templist.append(str)
        sublist.extend(templist)
        print('成功sublist=', sublist)

    if substr == '':
      print('成功num=', num)
      list.extend(sublist)
      sublist = []
      substr = strA[:]

    # return list


class TestView(ListView):
  form = TestForm()
  context_object_name = 'hotelList'

  def get(self, request, *args, **kwargs):
    super().get(self, request, *args, **kwargs)

    context = self.get_context_data()
    context['form'] = self.form

    return self.render_to_response(context)

  def post(self, request, *args, **kwargs):
    super().get(self, request, *args, **kwargs)
    context = self.get_context_data()
    context['form'] = TestForm(request.POST)

    formdata = context['form'].data.dict()
    inputA = formdata['inputA']
    inputB = formdata['inputB']
    print(fibo(5))
    # string to dict
    dict = ast.literal_eval(inputB)
    # print(dict[2:3])
    sublist = []
    list = []

    # print(inputA)
    # print(inputB)
    # substr = None
    '''
    start = 0
    for i in range(0, len(inputA)):
      substr = inputA[start: i + 1]

      # print(substr)
      if substr in dict:
        list.append(substr)
        substr = ''
        start = i + 1
    '''

    substr = inputA[:]
    a = dicSearch(substr, dict, list)
    # num = 1
    # for str in dict:
    #   # print('str', str)
    #   if substr.find(str) >= 0:
    #     sublist.append(str)
    #     substr = substr.replace(str, "", 1)
    #     subdic = dict[num:]
    #     if len(subdic) > 0:
    #       print('subdic', subdic)
    #     # sublist=[]
    #     # dic_search(substr,subdic)
    #     # print('subsub',sublists)
    #     # if len(sublist)>0:
    #     #   sublist.append(str)
    #     #   sublist.extend(sublists)
    #     #   list.extend(sublist)
    #     #   sublist = []
    #     #   substr = inputA[:]
    #   if substr == '':
    #     print('成功')
    #     list.extend(sublist)
    #     sublist = []
    #     substr = inputA[:]
    #   num = num + 1

    # print(len(list))
    # 三項演算子
    context['result1'] = '〇' if len(list) > 0 else 'X'
    # spaceでlist join
    context['result2'] = ' '.join(list) if len(list) > 0 else ''

    return self.render_to_response(context)

  def get_queryset(self):
    return []
