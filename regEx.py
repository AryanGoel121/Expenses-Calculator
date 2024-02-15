import re

pattern = "and"
text = """The Marvel Cinematic Universe (MCU) is an American media franchise and shared universe centered on a series of superhero films produced by Marvel Studios. The films are based on characters that appear in American comic books published by Marvel Comics. The franchise also includes television series, short films, digital series, and literature. The shared universe, much like the original Marvel Universe in comic books, was established by crossing over common plot elements, settings, cast, and characters.

Marvel Studios releases its films in groups called "Phases", with the first three phases collectively known as "The Infinity Saga" and the following three phases as "The Multiverse Saga". The first MCU film, Iron Man (2008), began Phase One, which culminated in the 2012 crossover film The Avengers. Phase Two began with Iron Man 3 (2013) and concluded with Ant-Man (2015). Phase Three began with Captain America: Civil War (2016) and concluded with Spider-Man: Far From Home (2019). Phase Four began with Black Widow (2021) and concluded with Black Panther: Wakanda Forever (2022). Ant-Man and the Wasp: Quantumania (2023) began Phase Five, which will end with Captain America: Brave New World (2025), and Phase Six will begin with The Fantastic Four (2025). Phase Six and "The Multiverse Saga" will conclude with Avengers 5 (2026) and Avengers: Secret Wars (2027)."""

match = re.search(pattern, text)
print(match)