# Imports you'll need.
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
import sys
import time
import twitter


  api = twitter.Api(consumer_key = 'cgzXf3uv155176JFvWFDPPTLQ',
  consumer_secret = 'XF7sNj92qfgB5RvM4FDEwk6bJEVjnPoQDM4ClZ8BVRqfVXA21u',
  access_token = '771404469372203008-LuQQIosZXnxSzTZKf8gZx2J13qalQKv',
  access_token_secret = 'o1U7MBSrB5MCVCO3mvSb860qoH7JexsYP98TjsjwjbRsX')

def read_screen_names(filename):
    """
    Read a text file containing Twitter screen_names, one per line.
    Params:
        filename....Name of the file to read.
    Returns:
        A list of strings, one per screen_name, in the order they are listed
        in the file.
    Here's a doctest to confirm your implementation is correct.
   
     read_screen_names('candidates.txt')
    ['DrJillStein', 'GovGaryJohnson', 'HillaryClinton', 'realDonaldTrump']
    """
    fh=open(filename,"r")
    return fh.read()
    
 
def get_users(twitter, screen_names):
    """Retrieve the Twitter user objects for each screen_name.
    Params:
        twitter........The TwitterAPI object.
        screen_names...A list of strings, one per screen_name
    Returns:
        A list of dicts, one per user, containing all the user information
        (e.g., screen_name, id, location, etc)
    See the API documentation here: https://dev.twitter.com/rest/reference/get/users/lookup
    In this example, I test retrieving two users: twitterapi and twitter.
    twitter = get_twitter()
    use=twitter.users.search(sc=screen_names)
    [u['id'] for u in users]
    twitter = get_twitter()
    
    users=api.GetFriends()
  """
def main():
    """ Main method. You should not modify this."""
    twitter = get_twitter()
    screen_names = read_screen_names('candidates.txt')
    print('Established Twitter connection.')
    print('Read screen names: %s' % screen_names)
    print api.VerifyCredentials() {"id": 16133, "location": "Philadelphia", "name": "bear"}
     """
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

# That's it for now! This should give you an introduction to some of the data we'll study in this course.
