from django import forms

from posts.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'title', 'text', 'image')
        labels = {
            'group': 'Группа записей',
            'text': 'Текст записи',
            'image': 'Картинка',
            'title': 'Заголовок'
        }
        help_texts = {
            'group': 'Выберите группу для записи '
                     '(по умолчанию без группы)',
            'text': 'Введите вашу запись сюда. Это поле '
                    'не должно быть пустым!',
            'image': 'Выберите картинку для вашей записи',
            'title': 'Введите заголовок сообщения',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Текст комментария'
        }
        help_text = {
            'text': 'Введите текст комментария'
        }
        widgets = {
            'text': forms.Textarea
        }
