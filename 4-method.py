class Movie:
    def __init__(self, title, yearLaunch, includedPlan, note, durationMinutes):
        self.title = title
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"{self.title} ({self.yearLaunch}) - {self.note} stars"

    def techinal_sheet(self):
        print("##Dados do filme##")
        print(f"Nome do filme: {self.title}")
        print(f"Ano de Lancamento: {self.yearLaunch}")
        print(f"Incluso no plano: {self.includedPlan}")
        print(f"Nota: {self.note}")
        print(f"Duração: {self.durationMinutes} minutos\n")


mario = Movie("Super Mario Bros", 1993, False, 2, 104)
top_gun = Movie("Top Gun Maverick", 2022, True, 4.5, 160)

mario.techinal_sheet()
top_gun.techinal_sheet()
