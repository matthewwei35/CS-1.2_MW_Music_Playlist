from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  def add_song(self, title):
    """Creates a Song object and adds it to the playlist. This method has one parameter called title."""
    new_song = Song(title)
    new_song.next = self.__first_song
    self.__first_song = new_song

  def find_song(self, title):
    """Searches for whether a song exists in the playlist and returns its index."""
    current_song = self.__first_song
    counter = 0
    while current_song != None:
      counter += 1
      if current_song.get_title() == title:
        return counter
      else:
        current_song = current_song.next
    return -1

  def remove_song(self, title):
    """Removes a song from the playlist. Takes title which is the song that should be removed."""
    current_song = self.__first_song
    if current_song.get_title() == title: 
      self.__first_song = current_song.get_next_song()
      return print(f"Removed song {title} from playlist.")
    else: 
      while current_song.get_title() != title:
        if current_song.get_title() == title: 
          current_song.set_next_song(current_song.get_next_song().get_next_song())
          return print(f"Removed song {title} from playlist.")
        else: 
          current_song = current_song.get_next_song()

  def length(self):
    """Returns the number of songs in the playlist."""
    current_song = self.__first_song
    counter = 0
    while current_song != None:
      counter += 1
      current_song = current_song.next
    return counter

  def print_songs(self):
    """Prints a numbered list of the songs in the playlist."""
    current_song = self.__first_song
    counter = 0
    if current_song == None:
      print("There are currently no songs in this playlist.")
    while current_song != None:
      counter += 1
      print(f"{counter}. {current_song.get_title()}")
      current_song = current_song.next

if __name__ == "__main__":
  playlist = Playlist()

  playlist.add_song("Hello")

  playlist.add_song("Hey")

  playlist.add_song("Hi")

  print(playlist.find_song("Hey"))

  print(playlist.find_song("Hi"))

  print(playlist.find_song("Hello"))

  print(playlist.find_song("Not In Here"))

  print(playlist.length())

  playlist.print_songs()

  print(playlist.remove_song("Hello"))

  playlist.print_songs()
