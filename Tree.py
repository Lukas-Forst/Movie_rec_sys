class TreeNode:
  def __init__(self, value):
    self.value = value
    self.movies = []
  def add_child(self, node):
    self.movies.append(node)
  def get_child(self):
    return self.movies
  def traverse(self):
    movie_node = self
    while movie_node.choices != []:
      choice = input("Enter 1 or 2 to continue the story: ")
      if choice not in ["1", "2"]:
        print("Enter a valid input")
      else:
        choice = int(choice)
        chosen_index = choice - 1
        chosen_child = movie_node.choices[chosen_index]
        print(chosen_child.story_piece)
        movie_node = chosen_child
