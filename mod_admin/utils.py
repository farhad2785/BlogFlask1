from flask import session,abort
from functools import wraps


def admin_only_view(func):
    @wraps(func)    # ----------> این دکوریتور برای این مباشد که از هر صفحه ای که دکوریتور
                    # ----------> admin_only_view
                    # ----------> صدا زده شود نام آن تغییر کند به تابع همان صفحه
    def decorator(*args, **kwargs):                 #   |
        if session.get('user_id') is None:          #   |
            abort(401)                              #   |
        if session.get('role') != 1:                #   |
            abort(403)                              #   |
        return func(*args, **kwargs)                #   |
    # print(decorator.__name__)                     #<--|
    return decorator