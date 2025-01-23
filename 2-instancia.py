class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    durationMinutes = 0


# Primeiro filme
movie = Movie()
movie.name = "The Godfather"
movie.yearLaunch = 1972
movie.includedPlan = True
movie.durationMinutes = 175
movie.note = 5.0

# Segundo filme
movie2 = Movie()
movie2.name = "The Godfather II"
movie2.yearLaunch = 1974
movie2.includedPlan = True
movie2.durationMinutes = 200
movie2.note = 4.9

print("##Dados do filme##")
print(f"Nome do filme: {movie.name}\nAno de Lancamento: {movie.yearLaunch}")
print(f"Nome do filme: {movie2.name}\nAno de Lancamento: {movie2.yearLaunch}")
