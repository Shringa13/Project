# Imports you'll need.
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
import sys
import time
from TwitterAPI import TwitterAPI


consumer_key = 'cgzXf3uv155176JFvWFDPPTLQ'
consumer_secret = 'XF7sNj92qfgB5RvM4FDEwk6bJEVjnPoQDM4ClZ8BVRqfVXA21u'
access_token = '771404469372203008-LuQQIosZXnxSzTZKf8gZx2J13qalQKv'
access_token_secret = 'o1U7MBSrB5MCVCO3mvSb860qoH7JexsYP98TjsjwjbRsX'


# This method is done for you. Make sure to put your credentials in the file twitter.cfg.
def get_twitter():
    """ Construct an instance of TwitterAPI using the tokens you entered above.
    Returns:
      An instance of TwitterAPI.
    """
    return TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)


def main():
    """ Main method. You should not modify this. """
    twitter = get_twitter()
    req = twitter.request('https://api.twitter.com/1/users/show.json?screen_name=TheSuggmeister&include_entities=true')
     print('Established Twitter connection.')
    """
    u= get_users(twitter,'Shringa13')
   
    screen_names = read_screen_names('candidates.txt')
    print('Established Twitter connection.')
    print('Read screen names: %s' % screen_names)
    
    users = sorted(get_users(twitter, screen_names), key=lambda x: x['screen_name'])
    print('found %d users with screen_names %s' %
          (len(users), str([u['screen_name'] for u in users])))
    add_all_friends(twitter, users)
    print('Friends per candidate:')
    print_num_friends(users)
    friend_counts = count_friends(users)
    print('Most common friends:\n%s' % str(friend_counts.most_common(5)))
    print('Friend Overlap:\n%s' % str(friend_overlap(users)))
    print('User followed by Hillary and Donald: %s' % followed_by_hillary_and_donald(users, twitter))

    graph = create_graph(users, friend_counts)
    print('graph has %s nodes and %s edges' % (len(graph.nodes()), len(graph.edges())))
    draw_network(graph, users, 'network.png')
    print('network drawn to network.png')
"""

if __name__ == '__main__':
    main()


 



