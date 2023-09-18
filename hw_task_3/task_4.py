class Apple:
    stages = ('flower', 'green', 'red')

    def __init__(self, index: int, stage: str = 'flower'):
        self.index = index
        if stage in self.stages:
            self.stage = stage
            self.__stage_index = self.stages.index(stage)
        else:
            raise NameError('Wrong stage, stage must be "flower", "green" or "red"')

    def is_grown(self):
        return self.stage == 'red'

    def grow(self):
        if not self.is_grown():
            self.__stage_index += 1
            self.stage = self.stages[self.__stage_index]


class Tree:
    def __init__(self, *args):
        self.apples = list(args)

    def grow(self):
        for apple in self.apples:
            apple.grow()

    def is_grown(self):
        return all([apple.is_grown() for apple in self.apples])

    def harwest(self):
        self.apples.clear()


class Gardener:
    def __init__(self, name: str, *args):
        self.name = name
        self.trees = list(args)

    def make_grow(self):
        for tree in self.trees:
            tree.grow()

    def gather(self):
        for tree in self.trees:
            if tree.is_grown():
                tree.harwest()
            else:
                print("WARNING! Tree is not fully grown yet")


t = Tree(Apple(0), Apple(1, 'green'), Apple(2, 'red'), Apple(3, 'flower'), Apple(4, 'red'))
g = Gardener('Bob', t)

g.make_grow()
g.make_grow()
g.gather()
