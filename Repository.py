
class Repository(object):
    def __init__(self):
        self._lg = 0
        self._graf = []
        self.load_from_file()

    def load_from_file(self):
        f = open("input.txt", "r")
        linii = f.readlines()
        self._lg = int(linii[0])
        for i in range(1, self._lg + 1):
            self._graf.append([int(j.rstrip()) for j in linii[i].split(',')])

    def write_to_file(self, problema):
        path1, cost1 = problema
        linii = [str(len(path1)) + '\n',
                 ','.join([str(nod) for nod in path1]) + '\n',
                 str(cost1) + '\n'
                 ]
        file = open('output.txt', 'w')
        file.writelines(linii)
        file.close()
        return 0

    def get_graf(self):
        return self._graf

    def get_lg(self):
        return self._lg
