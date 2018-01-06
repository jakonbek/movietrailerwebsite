import movie_website
import media

# instances of the Movies class
dunkirk = media.Movies("Dunkirk",
                        "A harrowing story of survival and resistance in World War II with skill and craft.",
                        "images/dunkirk.jpeg",
                        "https://www.youtube.com/watch?v=F-eMt3SrfFU",
                        "Action, Drama, History, War",
                        "PG-13")
ny_library = media.Movies("Ex Libris: The New York Public Library",
                          "A story about New York Public Library",
                          "images/ny_library.jpeg",
                          "https://www.youtube.com/watch?v=0UsglJmevFM",
                          "Documentary",
                          "Not Rated")
faces_places = media.Movies("Faces Places",
                            "Director Agnes Varda and photographer "
                            "and muralist JR journey through rural France "
                            "and form an unlikely friendship.",
                            "images/faces_places.jpeg",
                            "https://www.youtube.com/watch?v=KKbjnLpxv70",
                            "Documentary",
                            "PG")
the_florida_project = media.Movies("The Florida Project",
                                   "A storyline about childhood in shadows of Disney Land",
                                   "images/the_florida_project.jpg",
                                   "https://www.youtube.com/watch?v=WwQ-NH1rRT4",
                                   "Drama",
                                   "Not Rated")
get_out = media.Movies("Get Out",
                       "An exhilaratingly smart and scary freakout "
                       "about a black man in a white nightmare, "
                       "the laughs come easily and then go in for the kill.",
                       "images/get_out.jpg",
                       "https://www.youtube.com/watch?v=YfLSryEaAfw",
                       "Mystery/Thriller",
                       "Not Rated")
lady_bird = media.Movies("Lady Bird",
                         "A storyline about nurse who struggles with difficulties of the life",
                         "images/lady_bird.jpeg",
                         "https://www.youtube.com/watch?v=cNi_HC839Wo",
                         "Drama/Comedy",
                         "R")
# List of movies
movies = [
    dunkirk,ny_library,faces_places,
    the_florida_project, get_out,lady_bird
    ]

movie_website.open_movies_page(movies)

