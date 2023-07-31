from flask_login import login_required, current_user
#from flask import Blueprint, request, url_for, flash, redirect, abort, Response, current_app

#from pybossa.core import (project_repo, user_repo, task_repo, blog_repo,result_repo, webhook_repo, auditlog_repo)
from functools import wraps

#@login_required
def project_is_published(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        return 'checking project publish status'
    
    return decorated_function
