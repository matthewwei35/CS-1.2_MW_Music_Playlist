class Song:

  def __init__(self, title):
    self.__title = title
    self.__next_song = None


  # TODO: Create a getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  # TODO: Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    self.__title = title

  # TODO: Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.__next_song

  # TODO: Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self.__next_song = next_title

  # TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return f"The song title is {self.__title}"

  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return f"{self.__title} -> {self.__next_song}"

if __name__ == "__main__":
  song = Song("Halo")

  print(song.get_title())

  song.set_title("Hello")

  print(song.get_title())

  song.set_next_song("Hey")

  print(song.get_next_song())
