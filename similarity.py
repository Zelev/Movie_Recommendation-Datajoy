from math import sqrt
from operator import itemgetter


def calculate_for_user(user, list_from):
    '''
    Will calculate the complete set of sums needed in the pearson coefficient
    '''
    user_sum = sum([user[item] for item in list_from])
    user_sq_sum = sum([pow(user[item], 2) for item in list_from])
    user_denominator = (user_sq_sum - pow(user_sum, 2)) / len(list_from)
    return user_sum, user_sq_sum, user_denominator


def similarity_score(user1, user2):
    '''
    Calculates the Pearson Score between the two users
    in terms of the movies they have rate
    '''
    score = 0
    both_viewed = [item for item in user1.keys() if item in user2.keys()]
    num_viewed = len(both_viewed)

    if num_viewed != 0:
        user1_sum, user1_sq_sum, user1_denominator = calculate_for_user(user1, both_viewed)
        user2_sum, user2_sq_sum, user2_denominator = calculate_for_user(user2, both_viewed)
        
        xsum_users = sum([user1[item] * user2[item] for item in both_viewed])
        
        pearson_numerator = xsum_users - ((user1_sum * user2_sum) / num_viewed)
        pearson_denominator = sqrt(user1_denominator * user2_denominator)
        if pearson_denominator == 0:
            score = 0
        else:
            score = pearson_numerator / pearson_denominator

    return score


def recommend(user_id, all_users):
    '''
    Use the pearson correlation to find the movies the user haven't seen yet
    '''
    totals = {}
    sums = {}

    for other in all_users.keys():
        if other != user_id:
            score = similarity_score(all_users[user_id], all_users[other])
            if score > 0:
                for movie in all_users[other].keys():
                    if movie not in all_users[user_id].keys():
                        totals.setdefault(movie, 0)
                        totals[movie] += all_users[other][movie]
                        sums.setdefault(movie, 0)
                        sums[movie] += score

    rankings = [(total / sums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    recomendations = [movie for ranking, movie in rankings]
    return recomendations