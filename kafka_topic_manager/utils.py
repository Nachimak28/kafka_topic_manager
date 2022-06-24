def ensure_config_is_valid(conf: dict):
    """
    Checks if config is valid or not by checking if the 
    bootstrap.servers key is present and has a non-empty 
    string value. Does nothing if config is valid.
    If config is invalid in any way, it raises an exception
    """
    if isinstance(conf, dict):
        if 'bootstrap.servers' not in conf.keys():
            raise Exception('configuration must contain key(s) bootstrap.servers')
        else:
            if conf.get('bootstrap.servers', None) == None:
                raise Exception('bootstrap.servers value cannot be None')
            elif conf.get('bootstrap.servers', None) == '':
                raise Exception('bootstrap.servers balue cannot be empty')
    else:
        raise Exception(f'conf must be a dictionary not a {type(conf)}')
