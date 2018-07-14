from django.shortcuts import render
from django.views.generic import ListView

from .form import TestForm
import ast


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

    # string to dict
    dict = ast.literal_eval(inputB)
    sublist = []
    list = []

    # print(inputA)
    # print(inputB)
    substr = None
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
    for str in dict:
      # print('str', str)
      if substr.find(str) >= 0:
        sublist.append(str)
        substr = substr.replace(str, "")
      if substr == '':
        print('成功')
        list.extend(sublist)
        sublist = []
        substr = inputA[:]

    print(len(list))
    # 三項演算子
    context['result1'] = '〇' if len(list) > 0 else 'X'
    # spaceでlist join
    context['result2'] = ' '.join(list) if len(list) > 0 else ''

    return self.render_to_response(context)

  def get_queryset(self):
    return []
