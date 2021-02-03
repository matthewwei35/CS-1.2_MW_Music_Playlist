class Song:

  def __init__(self, title):
    self.__title = title
    self.__next_song = None


  def get_title(self):
    """Getter method that returns the title of a song."""
    return self.__title
  
  def set_title(self, title):
    """Setter method that sets the title of a song."""
    self.__title = title

  def get_next_song(self):
    """Getter method that returns next song."""
    return self.__next_song

  def set_next_song(self, next_title):
    """Setter method that sets the next song."""
    self.__next_song = next_title

  def __str__(self):
    """Returns a string representation of song."""
    return f"The song title is {self.__title}"

  def __repr__(self):
    """Returns a coder friendly representation of song."""
    return f"{self.__title} -> {self.__next_song}"

if __name__ == "__main__":
  song = Song("Halo")

  print(song.get_title())

  song.set_title("Hello")

  print(song.get_title())

  song.set_next_song("Hey")

  print(song.get_next_song())

  print(song.__str__())

  print(song.__repr__())
