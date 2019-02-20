

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


def flatten_dict(some_dict, delim='_'):
    def flatten_nested(key, value):
        if hasattr(value, 'items'):
            return [(key + delim + k, v) for k, v in flatten_dict(value).items()]
        else:
            return [(key, value)]

    return dict([item for k, v in some_dict.items() for item in flatten_nested(k, v)])


def prep_template_parameters(some_dict, **kwargs):
    return snake_keys_to_pascal(flatten_dict(copy_keys(some_dict, **kwargs)))


class FilterModule(object):
    def filters(self):
        return dict(
            copy_keys=copy_keys,
            flatten_dict=flatten_dict,
            snake_to_pascal=snake_to_pascal,
            snake_keys_to_pascal=snake_keys_to_pascal,
            prep_template_parameters=prep_template_parameters
        )
