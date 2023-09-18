from random import randrange


class Apple:
    stages = ('flower', 'green', 'red')

    def __init__(self, index: int, stage: str = 'flower'):
        self.over_age = 0
        self.index = index
        if stage in self.stages:
            self.stage = stage
            self.__stage_index = self.stages.index(stage)
        else:
            raise NameError('Wrong stage, stage must be "flower", "green" or "red"')

    def is_grown(self):
        return self.stage == 'red'

    def is_not_grown(self):
        return self.stage != 'red'

    def grow(self):
        if self.is_not_grown():
            self.__stage_index += 1
            self.stage = self.stages[self.__stage_index]
        else:
            self.over_age += 1

    def __repr__(self):
        return f'{self.stage} apple index {self.index} over age {self.over_age}'


class Tree:
    def __init__(self, *args, age=1):
        self.age = age
        self.apples = list(args)

    def grow(self):
        for apple in self.apples:
            apple.grow()
        if self.age > 9:
            self.apples.clear()
        elif self.age > 5:
            pass
        elif self.age > 2:
            if self.apples:
                self.apples.extend([Apple(self.apples[-1].index + i) for i in range(randrange(3))])
            else:
                self.apples.extend([Apple(i) for i in range(randrange(3))])
        self.age += 1
        self.apples = list(filter(lambda item: item.over_age <= 3, self.apples))

    def is_grown(self):
        return all([apple.is_grown() for apple in self.apples])

    def harwest(self):
        not_red = list(filter(Apple.is_not_grown, self.apples))
        self.apples = not_red

    def get_apples_info(self):
        return [apple.stage for apple in self.apples]


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
                tree.harwest()

    def get_trees_info(self):
        ages = [tree.age for tree in self.trees]
        return len(ages), ages

    def get_apples_info(self):
        res = []
        for tree in self.trees:
            res.extend(tree.get_apples_info())
        return len(res), res


t1 = Tree(Apple(0), Apple(1, 'green'), Apple(2, 'red'), Apple(3, 'flower'), Apple(4, 'red'))
t2 = Tree(age=2)
g = Gardener('Bob', t1, t2)


g.make_grow()
g.gather()
g.make_grow()
print(g.get_apples_info())
g.gather()
print(g.get_trees_info())
g.make_grow()
print(g.get_apples_info())
g.make_grow()
g.make_grow()
g.make_grow()
print(g.get_apples_info())
g.make_grow()
g.make_grow()
g.make_grow()
g.make_grow()
g.make_grow()
g.make_grow()
g.make_grow()
g.make_grow()
g.make_grow()
print(g.get_trees_info())
