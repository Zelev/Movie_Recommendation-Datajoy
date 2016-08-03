from read_data import read_file, get_ratexuser, get_movie_genres
from similarity import recommend
from user_personalization import print_question

data, labels = read_file()

# Get all the movie titles just one time
movies, genres = get_movie_genres(data, labels)

# separate the users by Id and then take just the ranking for each movie
data_dicts, user_ids = get_ratexuser(data)

print_question(data, labels, user_ids, data_dicts)

