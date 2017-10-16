import fresh_tomatoes
import media


the_social_network = media.Movie("The Social Network",
                        "The Social Network is a 2010 American biographical drama film directed by David Fincher and written by Aaron Sorkin. Adapted from Ben Mezrich's 2009 book The Accidental Billionaires: The Founding of Facebook, A Tale of Sex, Money, Genius, and Betrayal, the film portrays the founding of social networking website Facebook and the resulting lawsuits. It stars Jesse Eisenberg as founder Mark Zuckerberg, along with Andrew Garfield as Eduardo Saverin, Justin Timberlake as Sean Parker, and Armie Hammer as Cameron and Tyler Winklevoss. Neither Zuckerberg nor any other Facebook staff were involved with the project, although Saverin was a consultant for Mezrich's book.The film was released in the United States by Columbia Pictures on October 1, 2010.The Social Network received widespread acclaim, with critics praising its direction, screenplay, acting, editing and score. Although several people portrayed in the film criticized its historical inaccuracies, the film appeared on 78 critics Top 10 lists for 2010; of those critics, 22 had the film in their number-one spot, the most of any film in its year. Rolling Stone's Peter Travers said The Social Network is the movie of the year. But Fincher and Sorkin triumph by taking it further. Lacing their scathing wit with an aching sadness, they define the dark irony of the past decade. It was also Roger Ebert selection for the best film of the year.At the 83rd Academy Awards, the film received eight nominations, including Best Picture, Best Director for Fincher, and Best Actor for Eisenberg, and won three for Best Adapted Screenplay, Best Original Score, and Best Film Editing. The film also received awards for Best Motion Picture – Drama, Best Director, Best Screenplay, and Best Original Score at the 68th Golden Globe Awards",
                        "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                        "https://www.youtube.com/watch?v=2RB3edZyeYw")


avatar = media.Movie('Avatar',
                     'A SCI-FI Alien Movie.',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')


gi_joe_retaliation = media.Movie('G.I. Joe Retaliation',
                                 'G.I. Joe: Retaliation is a 2013 American military science fiction action film directed by Jon M. Chu and written by Rhett Reese and Paul Wernick, based on Hasbro G.I. Joe toy, comic, and media franchise. It is the second film in the G.I. Joe film series, and is a sequel to 2009 G.I. Joe: The Rise of Cobra, while also serving as a soft reboot of the franchise.Retaliation features an ensemble cast with Byung-hun Lee, Ray Park, Jonathan Pryce, Arnold Vosloo, and Channing Tatum reprising their roles from the first film. Luke Bracey and Robert Baker take over the role of Cobra Commander, replacing Joseph Gordon-Levitt. Dwayne Johnson, D. J. Cotrona, Adrianne Palicki, Ray Stevenson, and Bruce Willis round out the principal cast.In the film, with Cobra operative Zartan still impersonating the President of the United States, the terrorist organization is able to frame the Joes as traitors, and have them nearly annihilated in an airstrike. Cobra Commander places the world leaders under Cobra control, and gains access to their advanced warheads. Outnumbered and outgunned, the surviving Joes form a plan with the original G.I. Joe, General Joseph Colton, to overthrow the Cobra Commander and his allies',
                                 'https://upload.wikimedia.org/wikipedia/en/0/09/G.I._Joe_Retaliation.jpg',
                                 'https://www.youtube.com/watch?v=V2YMu52MfqA')

man_of_steel = media.Movie('Man of Steel',
                           'Man of Steel is a 2013 superhero film featuring the DC Comics character Superman. It is a British-American venture produced by Legendary Pictures, DC Entertainment, Syncopy Inc., and Cruel and Unusual Films, and distributed by Warner Bros. Pictures. It is the first installment in the DC Extended Universe. The film is directed by Zack Snyder, written by David S. Goyer, and stars Henry Cavill, Amy Adams, Michael Shannon, Kevin Costner, Diane Lane, Laurence Fishburne, Antje Traue, Ayelet Zurer, Christopher Meloni, and Russell Crowe. Man of Steel is a reboot of the Superman film series that retells the characters origin story. In the film, Clark Kent learns that he is a superpowered alien from the planet Krypton and assumes the role of mankind protector as Superman, but finds himself having to prevent General Zod from destroying humanity.',
                           'https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg',
                           'https://www.youtube.com/watch?v=T6DJcgm3wNY')

rush = media.Movie('Rush',
                   'Rush is a 2013 biographical sports action drama film centred on the rivalry between Formula 1 drivers James Hunt and Niki Lauda during the 1976 Formula One motor-racing season. It was written by Peter Morgan, directed by Ron Howard and stars Chris Hemsworth as Hunt and Daniel Brühl as Lauda. The film premiered in London on 2 September 2013 and was shown at the 2013 Toronto International Film Festival before its United Kingdom release on 13 September 2013',
                   'https://upload.wikimedia.org/wikipedia/en/d/d0/Rush_UK_poster.jpeg',
                   'https://www.youtube.com/watch?v=4XA73ni9eVs')

the_maze_runner = media.Movie('The Maze Runner',
                              'The Maze Runner is a 2014 American dystopian science fiction action thriller film directed by Wes Ball, in his directorial debut, based on James Dashner 2009 novel of the same name. The film is the first installment in The Maze Runner film series and was produced by Ellen Goldsmith-Vein, Wyck Godfrey, Marty Bowen, and Lee Stollman with a screenplay by Noah Oppenheim, Grant Pierce Myers, and T.S. Nowlin. The film stars Dylan O Brien, Kaya Scodelario, Aml Ameen, Thomas Brodie-Sangster, Ki Hong Lee, Will Poulter, and Patricia Clarkson. The story follows sixteen-year-old Thomas, portrayed by O Brien, who awakens in a rusty elevator with no memory of who he is, only to learn he is been delivered to the middle of an intricate maze, along with a large number of other boys, who have been trying to find their way out of the ever-changing labyrinth — all while establishing a functioning society in what they call the Glade.',
                              'https://upload.wikimedia.org/wikipedia/en/b/be/The_Maze_Runner_poster.jpg',
                              'https://www.youtube.com/watch?v=64-iSYVmMVY')

movies = [the_social_network, avatar, gi_joe_retaliation, man_of_steel, rush, the_maze_runner]
fresh_tomatoes.open_movies_page(movies)

