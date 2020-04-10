import random

from Chromosome import Chromosome


class Populatie:
    def __init__(self, repo):
        self.__repo = repo
        self.__populatie = self.genereazaPopulatie()

    @property
    def populatie(self):
        return self.__populatie

    def genereazaPopulatie(self):
        problParam = {'noNodes': self.__repo.get_lg()}
        rez = []
        for i in range(20):
            c = Chromosome(problParam)
            dist = 0
            nodPrecedent = c.repres[0]
            for nod in c.repres[1:]:
                dist += self.__repo.get_graf()[nodPrecedent - 1][nod - 1]
                nodPrecedent = nod
            dist += self.__repo.get_graf()[nodPrecedent-1][c.repres[0]-1]
            c.fitness = dist
            rez.append(c)
        return rez

    def selectie_reproducere(self):
        k = 0
        p = 0
        prob = {}
        ruleta = []
        suma = 0
        for individ in self.__populatie:
            suma += individ.fitness
        for individ in self.__populatie:
            k += 1
            prob[k] = [suma//individ.fitness, individ]
            for i in range(p, prob[k][0]):
                ruleta.append(k)
            p = k
        pos1 = random.choice(ruleta)
        pos2 = random.choice(ruleta)
        c1 = prob[pos1][1]
        c2 = prob[pos2][1]
        return c1, c2
