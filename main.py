from Populatie import Populatie
from Repository import Repository


def fct(e):
    return e.fitness


def rezolvare():
    repo = Repository()
    populatie = Populatie(repo)
    for i in range(10000):
        p1, p2 = populatie.selectie_reproducere()
        c1 = p1.crossover(p2)
        c1.mutation()
        dist = 0
        nodPrecedent = c1.repres[0]
        for nod in c1.repres[1:]:
            dist += repo.get_graf()[nodPrecedent - 1][nod - 1]
            nodPrecedent = nod
        dist += repo.get_graf()[nodPrecedent - 1][c1.repres[0] - 1]
        c1.fitness = dist
        if p1.fitness > c1.fitness and c1.repres[0] ==1:
            for k in range(len(populatie.populatie)):
                if populatie.populatie[k] == p1:
                    populatie.populatie[k] = c1
        if p2.fitness > c1.fitness and c1.repres[0] == 1:
            for k in range(len(populatie.populatie)):
                if populatie.populatie[k] == p2:
                    populatie.populatie[k] = c1
        populatie.populatie.sort(key=fct)
        print(populatie.populatie[0])
    populatie.populatie.sort(key=fct)
    repo.write_to_file([populatie.populatie[0].repres, populatie.populatie[0].fitness])


rezolvare()
