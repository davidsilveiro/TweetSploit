from twython import Twython, TwythonError
from time import sleep
from sys import exit

app_key             = ''
app_secret          = ''
oauth_token         = ''
oauth_token_secret  = ''

twitter = Twython(app_key, app_secret, \
	  oauth_token, oauth_token_secret)


def follow(username):
    

    """ So we loop through our the 'EXAMPLE' users followers    """
    """ and we proceed to fetch their ids, and finish off by    """
    """ wishing them a nice day. Also, the reason we wait for   """
    """ 180 seconds is because this sort of timing seemed to    """
    """ not irritate the hell out of Twitter's api limits.      """


    amount         = raw_input("Amount of users to follow: ")
    followers      = twitter.get_friend_ids(screen_name=username)
    amount_Counter = 0
    
    while amount_Counter <= amount:
        for ids in followers['ids']:

            try:
                t.create_friendship(user_id=ids)
                sleep(1)
                amount_Counter += 1
            except KeyboardInterrupt, TwythonError:
                exit()

    print("Finished following %s followers"% username)
    
    
def unfollow(username):

    amount         = raw_input("Amount of users to follow: ")
    followers      = twitter.get_friend_ids(screen_name=username)
    amount_Counter = 0

    while amount_Counter <= amount:
        for ids in followers['ids']:

            try:
                t.destroy_friendship(user_id=ids)
                sleep(1)
                amount_Counter += 1
            except KeyboardInterrupt, TwythonError:
                exit()

    print("Finished unfollowing %s followers"% username)
    

def favorite(hashtag):

    amount         = raw_input("Amount of posts to favorite: ")
    followers      = twitter.get_friend_ids(screen_name=hashtag)
    amount_Counter = 0

    while amount_Counter <= amount:
        for ids in followers['ids']:

            try:
                t.create_favorite(user_id=ids)
                sleep(1)
                amount_Counter += 1
            except KeyboardInterrupt, TwythonError:
                exit()

    print("Finished favoriting posts under %s "% hashtag)


def message(username):

    amount         = raw_input("Amount of users to follow: ")
    search_results = twitter.search(q=username, count=amount)
    amount_Counter = 0

    while amount_counter <= amount: 
        for tweet in search_results["statuses"]:
        	
            try:
                twitter.create_favorite(id = tweet["id_str"])
                time.sleep(5)
            except KeyboardInterrupt, TwythonError:
                exit()
                
    print("Finished messaging the followers of %s"% username)            



def main():

    print("Welcome to the Twython suite, a wrapper offering \n \
	   you an easy way to make use of the Twitter API")

    print("Author of Tweetsploit   : David Silveiro          \n \
    	   Auther of Twython Module: ryanmcgrath")

    print("Enter the number matching the option             \n \
    	   \n 1) Follow \n 2) Unfollow \n 3) Favorite          \
           \n 4) Message ")


    try:
        twitter = Twython(app_key, app_secret, \
	oauth_token, oauth_token_secret)
	
    except:
    	print("Keys might be invalid")


    option = int(raw_input("option:               "))



    if option == 1:
           

        username      = raw_input("Username:      ")
        follow(username)

    elif option  == 2:
  
        self_Username = raw_input("Your username: ")
        unfollow(self_Username)

    elif option  == 3:

        hashtag       = raw_input("Hashtag:       ")
        favorite(hashtag)

    elif option  == 4:

        self_Username = raw_input("Hashtag:       ")
        message(self_Username)

    else:
        print("Error, option %s is not recognised!"% option)


if __name__ == "__main__":
    main()
