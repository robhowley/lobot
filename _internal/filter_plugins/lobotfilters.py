

def snake_to_pascal(some_str):
    return ''.join([si.title() for si in some_str.split('_')])


def snake_keys_to_pascal(some_dict):
    return {snake_to_pascal(k): v for k, v in some_dict.items()}


def copy_keys(some_dict, include=None, exclude=None):
    should_keep = lambda k: (
        k not in (exclude or []) and
        k in (include or some_dict.keys())
    )
    return {k: v for k, v in some_dict.items() if should_keep(k)}


class FilterModule(object):
    def filters(self):
        return dict(
            copy_keys=copy_keys,
            snake_to_pascal=snake_to_pascal,
            snake_keys_to_pascal=snake_keys_to_pascal
        )
