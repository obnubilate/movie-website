import fresh_tomatoes
import media
# In line 1, the fresh_tomaties.py file is imported. In line 2, the media.py file is imported. fresh_tomatoes.py generates the html file; fresh_tomatoes.html, fresh_tomatoes.pyc (I believe), and media.pyc (I believe)
wolf_of_wall_st = media.Movie("Wolf of Wall St", "The rise and fall of superstar broker Jordan Belfort",
				  "https://media.giphy.com/media/x8hdR7wEoq6Qw/giphy.gif",
				  "https://www.youtube.com/watch?v=UTHlXb0PXh4")
#here, a class is made, the wolf of wall street from the media.py file (blueprint). In this information, the title is made ("the wolf of wall street"), secondly, the description of the movie is added as "The rise and fall of superstar broker Jordan Belfort",
#print(wolf_of_wall_st.storyline)

the_great_gatsby = media.Movie("The Great Gatsby", "The tragic story of Millionaire Jay Gatsby",
				  "http://pixel.nymag.com/imgs/daily/vulture/2015/gifs/leo-toast-9.w529.h352.gif",
				  "https://www.youtube.com/watch?v=rARN6agiW7o")
#here, another new class is made as derived from media.py; which is in this case; the great gatsby. It is described as "The tragic story of Millionaire Jay Gatsby", which can be verified by printing "print(wolf_of_wall_st.storyline)" on the console.


the_social_network = media.Movie("The Social Network", "A Harvard student builds a petty web application and gains substantial wealth and fame because of it",
				  "http://2.bp.blogspot.com/-7mAZpAqWKd8/VWmPBzwC0SI/AAAAAAAAMgw/XgGuKB3Lkzg/s1600/Facebook%2Bgif%2Bimage.gif",
				  "https://www.youtube.com/watch?v=lB95KLmpLR4")
#here, a new class is made that is derived from the media.py file (this is but a model derived from that blueprint). It's name is...quite obviously..."the social network". It is about "A Harvard student builds a petty web application and gains substantial wealth and fame because of it"
a_beautiful_mind = media.Movie("A Beautiful Mind", "The story of Princeton Mathematician, John Nash",
	              "http://i.imgur.com/ITsMmmk.gif",
	              "https://www.youtube.com/watch?v=aS_d0Ayjw4o")
# this movie class is also derived from media.py and is titled a beautiful mind, which; as described, is about the story of Princeton Mathematician John Nash (Who is, as a matter of fact, WAY less impressive to be after I discovered that he was only diagnosed with schizophrenia AFTER getting tenure at MIT, topkek.  )
the_imitation_game = media.Movie("The Imitation Game", "The story of legendary WWII Codebreaker, Alan Turing",
	              "https://s-media-cache-ak0.pinimg.com/originals/24/d5/b1/24d5b1deffe140e5ca2eaf12f815a10f.jpg",
	              "https://www.youtube.com/watch?v=S5CjKEFb-sM")
# again, this class is also derived from the media.py file and is titled "the imitation game" which is about Alan Turing, a badass WWII Codebreaker (as described within the code and can be verified by typing in print(the_imitation_game.storyline) and building it~
the_man_who_knew_infinity = media.Movie("The Man Who Knew Infinity", "A story showcasing the life of Srinivasa Ramanujan, an obscure, self-taught mathematician from India",
	              "https://s-media-cache-ak0.pinimg.com/originals/1a/1f/d5/1a1fd5698898700e2230e6cfef2235a5.jpg",
	              "https://www.youtube.com/watch?v=kLEyxQv3l0U")
#lastly, (phew!) this class (above in lines 28-30), is about a superbly intelligent mathematician from India who discovered alot of maths on his own "as described by the .storyline". This is a class derived from media.py
movies = [wolf_of_wall_st, the_great_gatsby, the_social_network, a_beautiful_mind, the_imitation_game, the_man_who_knew_infinity]
fresh_tomatoes.open_movies_page(movies)
