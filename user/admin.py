from django.contrib import admin  # 장고에서 admin 툴을 사용하겠다
from .models import UserModel  # 지금 우리 위치와 동일하게 있는 models라는 파이썬 파일을 불러오겠다.

# Register your models here.
admin.site.register(UserModel)  # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
