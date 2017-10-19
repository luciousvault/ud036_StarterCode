import webbrowser


class Movie():
    """This class represents a movie object. Movies tend to have a title,
    storyline, poster image, and a trailer."""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """self is the object being created. We can establish fields
        by using the self reference with a '.' and the name of the
        field to establish being set to a value. A helpful convention
        is to name the field simular to the passed in parameters.
        Ex. : 'self.title = movie_title' """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """The show_trailer function opens up a browser and displays the
        content in a new tab."""
        webbrowser.open(self.trailer_youtube_url)
