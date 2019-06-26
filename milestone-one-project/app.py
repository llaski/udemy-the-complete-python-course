"""
a
l
f
q

get input
add movie
list movies
find movie
stop running program
"""

movies = []

"""
movie = {
    'name': ...(str),
    'director': ...(str),
    'year': ...(int),
}
"""


def menu():
    user_input = input(
        "Enter 'a' to add movie, 'l' to see your movies, 'f' to find movie', and 'q' to quit: ")

    while user_input != 'q':

        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command - please try again')

        user_input = input(
            "\nEnter 'a' to add movie, 'l' to see your movies, 'f' to find movie', and 'q' to quit: ")


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = int(input("Enter the movie year: "))

    movies.append({
        'name': name,
        'director': director,
        'year': year,
    })


def show_movies():
    for movie in movies:
        print_movie_details(movie)


def print_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}\n")


menu()

print(movies)
