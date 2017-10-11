import media
import fresh_tomatoes

# I liked Toy Story as a movie growing up.
# I think it was the first movie I saw in theater.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toysthat come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/"
                        + "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
princessbride = media.Movie("Princess Bride",
                     "A fairy tale adventure about a beautiful young woman "
                        + "and her one true love. He must find her after "
                        + "a long separation and save her. They must "
                        + "battle the evils of the mythical kingdom "
                        + "of Florin to be reunited with each other."
                        + " Based on the William Goldman novel 'The "
                        + "Princess Bride' which earned its own loyal "
                        + "audience.",
                     "http://quotesta.com/wp-content/uploads/"
                        + "Princess-Bride-Poster-Original-1-1.jpg",
                     "https://www.youtube.com/watch?v=VYgcrny2hRs")
riddick = media.Movie("Riddick",
                       "Riddick fights to survive and leave another "
                       + "inhospitable planet",
                       "http://cdn.collider.com/wp-content/uploads/"
                       + "riddick-poster-3.jpg",
                       "https://www.youtube.com/watch?v=ljKLtkSbIKY")
matrix = media.Movie("The Matrix",
                     "Neo (Keanu Reeves) believes that Morpheus "
                     + "(Laurence Fishburne), an elusive figure considered "
                     + "to be the most dangerous man alive, can answer his "
                     + "question -- What is the Matrix? Neo is contacted by"
                     + " Trinity (Carrie-Anne Moss), a beautiful stranger "
                     + "who leads him into an underworld where he meets "
                     + "Morpheus. They fight a brutal battle for their lives"
                     + " against a cadre of viciously intelligent secret "
                     + "agents. It is a truth that could cost Neo something "
                     + "more precious than his life.",
                     "https://images-na.ssl-images-amazon.com/images/I/"
                     + "51FhdGyJ6DL._SL500_AC_SS350_.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")
# oldboy url might get taken down due to copyright.
oldboy = media.Movie("Oldboy",
                     "Dae-Su is an obnoxious drunk bailed from the police "
                     + "station yet again by a friend. However, he's "
                     + "abducted from the street and wakes up in a cell, "
                     + "where he remains for the next 15 years, drugged "
                     + "unconscious when human contact is unavoidable, "
                     + "otherwise with only the television as company. And "
                     + "then, suddenly released, he is invited to track "
                     + "down his jailor with a denouement that is simply "
                     + "stunning.",
                     "http://img.moviepostershop.com/oldboy-movie-poster"
                     + "-2003-1020263711.jpg",
                     "https://www.youtube.com/watch?v=D89OHw0VsYM")
raid = media.Movie("The Raid Redemption",
                   "A rookie member of an elite team of commandos,Rama" 
                   + "(Iko Uwais) is instructed to hang back while his"
                   + "comrades-in-arms go ahead with their mission to take "
                   + "down a brutal crime lord called Tama (Ray Sahetapy). "
                   + "However, the team's cover is blown, and Tama offers "
                   + "sanctuary to every criminal in his high-rise apartment "
                   + "block in exchange for the cops' heads. Now Rama must "
                   + "take command and lead his remaining team on an "
                   + "ultraviolent charge through the building to complete "
                   + "-- and survive -- the mission.",
                   "http://www.joblo.com/posters/images/full/raid-australian"
                   + "-poster.jpg",
                   "https://www.youtube.com/watch?v=m6Q7KnXpNOg")
battle_royale = media.Movie("Battle Royale",
                            "In the future, the Japanese government captures"
                            + " a class of ninth-grade students and forces "
                            + "them to kill each other under the "
                            + "revolutionary \"Battle Royale\" act.",
                            "https://resizing.flixster.com/boY6Rc6NtlDVQoQw"
                            + "BzteIslnkVY=/206x305/v1.bTsxMTM3NjE3ODtqOzE3"
                            + "NTAxOzEyMDA7OTAwOzEyMDA",
                            "https://www.youtube.com/watch?v=N0p1t-dC7Ko")
kill_bill = media.Movie("Kill Bill Vol. 1",
                        "The lead character, called 'The Bride,' was a member"
                        + " of the Deadly Viper Assassination Squad, led by "
                        + "her lover 'Bill.' Upon realizing she was pregnant "
                        + "with Bill's child, 'The Bride' decided to escape "
                        + "her life as a killer. She fled to Texas, met a young"
                        + " man, who, on the day of their wedding rehearsal was"
                        + " gunned down by an angry and jealous Bill (with the "
                        + "assistance of the Deadly Viper Assassination Squad)."
                        + " Four years later, 'The Bride' wakes from a coma, "
                        + "and discovers her baby is gone. She, then, decides "
                        + "to seek revenge upon the five people who destroyed "
                        + "her life and killed her baby. The saga of Kill Bill "
                        + "Volume I begins.",
                        "http://s2.thingpic.com/images/xr/yJbD1JBhmpbD5AK2"
                        + "mW6Aq95U.jpeg",
                        "https://www.youtube.com/watch?v=7kSuas6mRpk")
boondock_saints = media.Movie("Boondock Saints",
                              "Two Irish brothers accidentally kill mafia "
                              + "thugs. They turn themselves in and are "
                              + "released as heroes. They then see it as a "
                              + "calling by God and start knocking off mafia"
                              + " gang members one by one. Willem Dafoe plays"
                              + " the detective trying to figure out the "
                              + "killings, but the closer he comes to catching"
                              + " the Irish brothers, the more he thinks the "
                              + "brothers are doing the right thing.",
                              "https://images-na.ssl-images-amazon.com/images"
                              + "/I/51lgZ0YTcQL.jpg",
                              "https://www.youtube.com/watch?v=ydXojYfCF3I")


movies = [toy_story, princessbride, riddick, matrix, oldboy, raid,
          battle_royale, kill_bill, boondock_saints]
fresh_tomatoes.open_movies_page(movies)

# Citation/Explanation:
# Movie storyline are mostly pulled from IMDB Plot page for the movie
# discribed. By searching the title of the movie on http://www.imdb.com and
# selecting the "Plot Summary" link you can find the plot page. Most of the
# plot descriptions are user written. I'm using the Summarys under the
# Educational portion of the Fair Use Act.
