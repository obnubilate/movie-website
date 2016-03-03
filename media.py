import webbrowser
#inb4 on lines 5-8 the self in .self.title etc is redundant and can be called anything...yay... :) 
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
#this is the blueprint that we will import in the entertainment_center.py file to make new movies! Yay! <(^_^<)
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		#This little command opens the webbrowser with .open (listed on python webpage; yay), ~line 11