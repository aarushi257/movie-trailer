import webbrowser
class Movie():
    """This class provides a way to store movie information."""
    def __init__(self, title, storyline, image, youtube_trailer):
        self.title = title   #Initializing values.
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = youtube_trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)   #Open function included in the webbrowser python library.
