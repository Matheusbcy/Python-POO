class Movie:
    def __init__(self, title, yearLaunch, includedPlan, durationMinutes):
        self.title = title
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"{self.title} ({self.yearLaunch}) - {self.note} stars"

    def techinal_sheet(self):
        print("##Dados do filme##")
        print(f"Nome do filme: {self.title}")
        print(f"Ano de Lancamento: {self.yearLaunch}")
        print(f"Incluso no plano: {self.includedPlan}")
        print(f"Avaliacao do Filme: {self.totalEvaluation}")
        print(f"Duração: {self.durationMinutes} minutos")
        print(f"Total de Avaliadores: {self.evaluators}\n")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Media do filme {self.title}: {self.totalEvaluation / self.evaluators}")


mario = Movie("Super Mario Bros", 1993, False, 104)
avatar = Movie("Avatar", 2009, True, 162)
mario.evaluate(9.5)
mario.evaluate(10)
mario.techinal_sheet()
mario.average()

avatar.evaluate(8)
avatar.evaluate(7)
avatar.techinal_sheet()
avatar.average()

#F090