from wtforms.form import Form
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets
from . import db
from . import models

class LoginForm(Form):
   name = simple.StringField(
       label = '用户名',
       validators=[
           validators.DataRequired(message='用户名不能为空')
       ],
       widget = widgets.TextInput(),
       render_kw={'class':"form-control"}
   )

   password = simple.PasswordField(
       label='密码',
       validators=[
           validators.DataRequired(message='密码不能为空')
       ],
       widget=widgets.PasswordInput(),
       render_kw={'class': "form-control"}
   )

   # def validate_password(self,field):
   #     res = db.session.query(models.UserInfo).filter(models.UserInfo.name == self.data['name'],
   #                                                    models.UserInfo.password == field.data).first()
   #     if not res:
   #         raise validators.StopValidation("用户名或密码错误")
