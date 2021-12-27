
from video_data import genres, movies
import itertools
import time
from Tree import TreeNode
# ASCII Art created with https://patorjk.com/software/taag/#p=testall&f=JS%20Bracket%20Letters&t=%20to%20the%20
"""
What does your program do?
recommend Movies of all available genres from the moviedb
https://www.themoviedb.org/
"""
def greet():
    print("""
  
 __          __  _                          
 \ \        / / | |                         
  \ \  /\  / /__| | ___ ___  _ __ ___   ___ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \/
    \  /\  /  __/ | (_| (_) | | | | | |  __/
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|
                                                                                   
   _          _   _           
  | |        | | | |          
  | |_ ___   | |_| |__   ___  
  | __/ _ \  | __| '_ \ / _ \ 
  | || (_) | | |_| | | |  __/ 
   \__\___/   \__|_| |_|\___| 
                              
  __  __         _                                              _      _   _          
 |  \/  |_____ _(_)___   _ _ ___ __ ___ _ __  _ __  ___ _ _  __| |__ _| |_(_)___ _ _  
 | |\/| / _ \ V / / -_) | '_/ -_) _/ _ \ '  \| '  \/ -_) ' \/ _` / _` |  _| / _ \ ' \ 
 |_|  |_\___/\_/|_\___| |_| \___\__\___/_|_|_|_|_|_\___|_||_\__,_\__,_|\__|_\___/_||_|
 
                _                 
               | |                
  ___ _   _ ___| |_ ___ _ __ ___  
 / __| | | / __| __/ _ \ '_ ` _ \ 
 \__ \ |_| \__ \ ||  __/ | | | | |
 |___/\__, |___/\__\___|_| |_| |_|
       __/ |                      
      |___/                       
                                                                                     
    """)


def display_genres():
    time.sleep(3)
    print("The following movie genres are available to watch: \n")
    genre_reg = 1
    for genre in genres:
        print(f"{genre_reg} \t {genre}")
        genre_reg += 1
    print("\n")



######################
### Create Tree Node##
######################

Root_Node = TreeNode("Movies")

for genre in genres:
    name = genre
    name = TreeNode(name)
    Root_Node.add_child(name)
    for movie in movies:
        if movie[-1] == genre:
            test = TreeNode(movie)

            name.add_child(test)

    #print(name.value)

print(Root_Node.get_child()[0].get_child()[0].value)



def get_genre():

    chosen_genre = input("Which movie genre would you like to watch today? \nYou can either input the beginning letters or the number corresponding to the genre.\n")

    # Validate input
    if chosen_genre.isnumeric() and int(chosen_genre) < 17:

        genre = Root_Node.get_child()[int(chosen_genre)-1]
        print(f"Your selected genre is {genre}")
        print("\n")
        again = input(f"Would you like to see a list of movies from the genre: {genre}? Enter 'y' for yes and 'n' for no ")
        if again == "y":
            get_movie(genre)
        else:
            get_genre()

    elif chosen_genre.isalpha():
        ind = len(chosen_genre)
        if ind == 1:
            genre = [genre.value for genre in Root_Node.get_child() if chosen_genre[ind-1].upper() == genre.value[ind-1].upper()]
            print(f"The following genres are beginning with your input: {genre}. \n")
            if len(genre) > 1:
                get_genre()
            else:
                again = input(f"Would you like to see a list of movies from the genre {genre[0]}? Enter 'y' for yes and 'n' for no ")
                if again == "y":
                    #print()
                    get_movie(genre)
                else:
                    get_genre()
            return genre
        elif ind > 1:
            genre = [genre.value for genre in Root_Node.get_child() if chosen_genre[:ind].upper() == genre.value[:ind].upper()]
            if genre:


                if len(genre) > 1:
                    get_genre()
                elif ind > 1:
                    print("\n")
                    again = input(f"Would you like to see a list of movies from {genre[0]}? Enter 'y' for yes and 'n' for no ")
                    if again == "y":
                        get_movie(genre)
                    else:
                        get_genre()
            else:
                print(f"Can't find a genre starting with {chosen_genre} \n")
                print("\n")
                get_genre()
        else:
            print(f"Can't find a genre starting with {chosen_genre} \n")
            print("\n")
            get_genre()
            #return genre
    else:
        print("The input is not recognized, try again. \n")
        print("\n")
        get_genre()

def get_genre_index(value):
    if type(value) == list:
        return [Root_Node.get_child().index(genre) for genre in Root_Node.get_child() if value[0] == genre.value][0]
    else:
        return [Root_Node.get_child().index(genre) for genre in Root_Node.get_child() if value == genre.value][0]

def get_movie(genre):
    print(genre)
    genre_index = get_genre_index(genre)
    print(genre_index)
    valid_movies = [movies.value for movies in Root_Node.get_child()[genre_index].get_child()]



    movie_amount = input("How many movie recommendation do you want to get? ")
    print("\n")
    print(valid_movies)
    return display_movies(valid_movies, movie_amount)


def display_movies(movie_list, display_am):
    #print(len(movie_list))
    display_am = int(display_am)
    for movie in range(0, display_am):
        print(f"""
Title: {movie_list[movie][0]}
Rating: {movie_list[movie][1]} / 10
Movie releases date: {movie_list[movie][2]}
Short Desc.: {movie_list[movie][4]}
        
===============================================
        """)
        #print(movie)
    again = input(f"Would you like to see other movies from a different genre? Enter 'y' for yes and 'n' for no \n")
    if again == "y":
        get_genre()
    else:
        end_rec()

def end_rec():
    print("Thank you for using the recommendation system hope you enjoyed it.")

greet()
display_genres()
get_genre()



