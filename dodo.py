
DOIT_CONFIG = {
    'default_tasks': [
        'flake8', 'unittest',
    ],
}


def task_flake8():
    """Run flake8 check."""
    return {
        'actions': ['flake8 a.py'],
    }


def task_unittest():
    return {
        'actions': ['python -m unittest']
    }


def task_all():
    return {
        'actions': None,
        'task_dep': ['flake8', 'unittest']
    }
