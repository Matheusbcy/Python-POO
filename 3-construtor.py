class Movie:
    def __init__(self, title, yearLaunch, includedPlan, note, durationMinutes):
        self.title = title
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
        
    def __str__(self):
        return f"{self.title} ({self.yearLaunch}) - {self.note} stars"
    
movie = Movie("Interstellar", 2014, False, 8.6, 169)
movie2 = Movie("Inception", 2010, True, 8.8, 148)

print(movie)
print(movie2)