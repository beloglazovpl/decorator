from datetime import datetime


def log_decor(param):
    def outer(func):
        def wrapper(*args, **kwargs):
            now = datetime.now()
            name = func.__name__
            result = func(*args, **kwargs)
            with open(f'{param}', 'a') as f:
                text = f'{now} --- {name} --- {args, kwargs} --- {result}\n'
                f.write(text)
            return result
        return wrapper
    return outer
