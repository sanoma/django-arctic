import os
import shutil
import tempfile
from subprocess import call


def test_start_new_project():
    """
    Test creating a new project with project bootstrap command.
    """
    project_name = 'test_arctic_project'
    project_path = tempfile.mkdtemp()
    manage_py_bin = os.path.join(project_path, 'manage.py')

    # remove DJANGO_SETTINGS_MODULE form env or arctic command will try loading
    # 'example.settings' module.
    env = os.environ.copy()
    env.pop('DJANGO_SETTINGS_MODULE')

    args = ['arctic', 'start', project_name, project_path]
    retcode = call(args, env=env)

    assert retcode == 0
    assert os.path.exists(manage_py_bin)

    # run Django system checks of generated project
    args = [manage_py_bin, 'check']
    retcode = call(args, env=env)
    assert retcode == 0

    # run Django migrations of generated project
    args = [manage_py_bin, 'migrate']
    retcode = call(args, env=env)
    assert retcode == 0

    """
    Test creating a new app with createapp bootstrap command.
    """
    app_name = 'newapp'
    app_path = project_path + '/new_app'
    os.mkdir(app_path)
    apps_py_bin = os.path.join(app_path, 'apps.py')

    args = ['arctic', 'createapp', app_name, app_path]
    retcode = call(args, env=env)

    assert retcode == 0
    assert os.path.exists(apps_py_bin)

    # cleanup test data
    shutil.rmtree(project_path)
