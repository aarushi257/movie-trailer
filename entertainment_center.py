import media
import fresh_tomatoes   #File which takes in the list of movies and generates an HTML file producing a website.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar","A marine on an alien planet",
                    "avatar.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock",
                            "An amateur rock enthusiast, slyly takes up his friend's substitute teacher's job.",
                            "school_of_rock.jpg",
                            "https://www.youtube.com/watch?v=LqEszt5wG9I")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Gil arrives with his fiancee and her family in Paris for a vacation and is beguiled by the city, which takes him away from his fiancee.",
                                "midnight.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")
a_walk_to_remember = media.Movie("A Walk to Remember",
                                 "A boy whose punishment involves participating in the spring play, during which he falls in love.",
                                 "a_walk_to_remember.jpg",
                                 "https://www.youtube.com/watch?v=i72wRvPw_ik")
a_notebook = media.Movie("A Notebook",
                         "Duke reads the story of Allie and Noah, two lovers who were separated by fate.",
                         "The_notebook.jpg",
                         "https://www.youtube.com/watch?v=FC6biTjEyZw")

movies = [toy_story,avatar,school_of_rock,midnight_in_paris,a_walk_to_remember,a_notebook]
fresh_tomatoes.open_movies_page(movies)  #Function which takes list as an arguement
