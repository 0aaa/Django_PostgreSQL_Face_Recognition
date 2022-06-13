from django.forms import FileField, Form


class RecognitionForm(Form):
    to_recognize = FileField()

    def get_to_recognize(self):
        return self.cleaned_data['to_recognize']