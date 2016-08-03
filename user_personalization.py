from read_data import read_file, get_ratexuser, get_movie_genres
from similarity import recommend as rec
from random import choice


def existing_user(movies, user_id, data_dicts, ranks = []):
    recommend = select_movie_recommendation(movies, ranks)
    rank = calification_movie(recommend)
    data_dicts = add_data_dict(user_id, rank, data_dicts)
    return rec(user_id, data_dicts), data_dicts


def select_movie_recommendation(movie_names, view):
    recommend = []
    while len(recommend) < 10:
        ran = choice(range(len(movie_names)))
        if not (movie_names.keys()[ran] in view):
            recommend.append(movie_names.keys()[ran])
    return recommend

    
def calification_movie(recommend):
    rank = {}
    counter = 1
    for movie in recommend:
        ranking = 0
        print(str(counter) + '. Did you like the movie '+ movie + '? ')
        while not ranking in xrange(1, 6):
            print 'Please enter a number between 1-5'
            ranking = int(input())
        rank[movie] = ranking
        counter += 1
    return rank

  
def add_data_dict(new_id, rank, data_dicts):
    data_dicts[new_id] = {}
    data_dicts[new_id] = {movie: rank[movie] for movie in rank.keys()}
    return data_dicts


def print_question(data, labels, user_ids, data_dicts):
    option = 0
    movies, genres = get_movie_genres(data, labels)
    while(option != 2 and option != 1):
        print ('Are you registered in the system? \n1 for Yes \n2 for No')
        try:
            option = int(input())
        except:
            print 'Please try Again, we could not understand the input'
            continue
    if option == 1:
        new_id = 0
        while not new_id in user_ids:
            print ('Enter id assigned: ')
            try:
                new_id = int(input())
            except:
                print 'Please Enter a correct Id'
                continue
        recomendations, data_dicts =  existing_user(movies=movies, user_id=new_id,
                                        ranks=data_dicts[new_id].keys(), 
                                        data_dicts=data_dicts)
    else:
        new_id = max(user_ids) + 1
        recomendations, data_dicts = existing_user(movies=movies, user_id=new_id,
                                                   data_dicts=data_dicts)
    print 'We recomend the next movies for you:'
    for x in recomendations[:5]:
        print x
