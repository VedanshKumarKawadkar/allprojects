from django.urls import path
from coding_playground import views


urlpatterns = [
    path("", view=views.home, name="home"),
    path("editor", view=views.editor, name="editor"),
    path("login", view=views.login, name="login"),
    path("runcode", view=views.runCode, name="runcode"),
    path("signup", view=views.signup, name="signup")
]
