def read_file():
    raw_data = [line for line in open('dataUser_nocomma.csv', 'r')]
    labels = raw_data[0].split(';')
    data = [x.split(';') for x in raw_data[1:]]
    return data, labels


def get_ratexuser(data):
    user_ids = set([int(x[1]) for x in data])
    data_dicts = {x: {} for x in user_ids}
    for data_entry in data:
        data_dicts[int(data_entry[1])][data_entry[8]] = int(data_entry[2])
    return data_dicts, user_ids

   
def get_movie_genres(data, labels):
    genres = labels[11:]
    movie_names = {x[8]: [] for x in data}
    movie_names = {x[8]: x[11:] for x in data if movie_names[x[8]] == []}
    return movie_names, genres