

def snake_to_pascal(some_str):
    return ''.join([si.title() for si in some_str.split('_')])


def snake_keys_to_pascal(some_dict):
    return {snake_to_pascal(k): v for k, v in some_dict.items()}


class FilterModule(object):
    def filters(self):
        return dict(
            snake_to_pascal=snake_to_pascal,
            snake_keys_to_pascal=snake_keys_to_pascal
        )
