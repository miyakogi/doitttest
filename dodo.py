def task_flake8():
    return {'actions': ['flake8 a.py']}


def task_unittest():
    return {'actions': ['python -m unittest']}


def task_all():
    return {'actions': None, 'task_dep': ['flake8', 'unittest']}
