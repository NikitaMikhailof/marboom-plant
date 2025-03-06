from django import forms


class SearchForm(forms.Form):
    query = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'id': 'search',
                'name': 'search',
                'type': 'text',
                'placeholder': 'введите запрос'
        })