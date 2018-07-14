from django import forms


class TestForm(forms.Form):
  inputA = forms.CharField(
      required=False,
      label='A',
      max_length=200,
      widget=forms.TextInput(
          attrs={
              'class': 'form-control',
              'placeholder': 'A',
              'style': 'max-width: 200px'
          }
      )
  )
  inputB = forms.CharField(
      required=False,
      label='B',
      max_length=200,
      widget=forms.TextInput(
          attrs={
              'class': 'form-control',
              'placeholder': 'B',
              'style': 'max-width: 200px'
          }
      )
  )
