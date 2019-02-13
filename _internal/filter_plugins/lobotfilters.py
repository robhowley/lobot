

def snake_to_pascal(some_str):
    return ''.join([si.title() for si in some_str.split('_')])


def snake_keys_to_pascal(some_dict):
    return {snake_to_pascal(k): v for k, v in some_dict.items()}


def copy_keys(some_dict, exclude=None):
    return {k: v for k, v in some_dict.items() if k not in (exclude or [])}


class FilterModule(object):
    def filters(self):
        return dict(
            copy_keys=copy_keys,
            snake_to_pascal=snake_to_pascal,
            snake_keys_to_pascal=snake_keys_to_pascal
        )
