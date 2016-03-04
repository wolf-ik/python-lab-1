class Storage(object):
    _set = set()
    _working = False

    def run(self):
        self._working = True
        while self._working:
            data = raw_input().split(' ')
            command = data[0]
            args = data[1:]
            func = self._command_mapping.get(command)
            if func is None:
                print('Invalid command.')
            else:
                print(func(self, *args))

    def add(self, *args):
        self._set.update(set(args))
        return 'Added.'

    def remove(self, *args):
        if len(args) >= 1:
            key = args[0]
        else:
            return 'Invalid arguments.'
        try:
            self._set.discard(key)
        except KeyError:
            return 'Not found.'
        return 'Deleted.'

    def find(self, *args):
        return ' '.join(self._set.intersection(set(args)))

    def list(self, *args):
        return ' '.join(self._set)

    def exit(self, *args):
        self._working = False
        return 'Stoped.'

    _command_mapping = {
        'add': add,
        'remove': remove,
        'find': find,
        'list': list,
        'exit': exit,
    }
