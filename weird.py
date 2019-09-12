class mulArgs:


    def __init__(self, *args, **kwargs):
        for index, value in enumerate(args):
            setattr(self, "p"+str(index), value)


class mulKwargs:


    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)


mulArgs(1)
mulArgs(1, 2)
mulArgs(1, 2, 3)
mulKwargs(clever=23, not_clever=42, why=108)