# Uncomment the following lines if you run the optional run_file tests locally
# so the input shows up in the output file. Do not copy these lines into Codio.
#
#import sys
#def input( prompt=None ):

 #   if prompt != None:
  #     print( prompt, end="" )
   # aaa_str = sys.stdin.readline()
    #aaa_str = aaa_str.rstrip( "\n" )
    #print(aaa_str)
    #return aaa_str
#
''' ###########################################################
#  Computer Project #5
#
# Algorithm
#  Program that can automatically suggest possible new connections
#  ( i.e., friends) for each user. For each user, this program suggests the most probable user
#  encrypted and decrypted using a combination of Affine and Caesar Cipher.
# to befriend based upon the intersection of your common friends
#
########################################################### '''



def open_file():
    ''' Ask the user for thye name of the file and open it
    if file not exist print an error statement and ask
    again until a correct file name is entered
    returns the file pointer '''
    while True:
        try:
            file_obj = open(input("\nEnter a filename: "))
            return file_obj
        except:
            print("\nError in filename.")
            continue


def read_file(fp):
    ''' loop through each line of the file
          take the numuber of users on first interation
                loop to create n_users number of list inside the newtork
          after every other consecutive iteration of each line,
                split the line into list
                find the user(u) and friend(v) on each line
                append each into the list of the other
                i.e place u in the list of v and v in list of until
        return network of list of lists of users and their friends  '''
    network = []
    count = 0
    for i in fp.readlines():
        count += 1
        if count == 1:
            i.strip()
            user_num = int(i)
            for index in range(user_num):
                network.append(list())

        else:
            i = i.strip().split()
            line = list(i)
            u = line[0]
            v = line[1]
            network[int(u)].append(int(v))
            network[int(v)].append(int(u))
    return network





def num_in_common_between_lists(list1, list2):
    ''' loop for each element in list1
            check if that element in list2 and append to an common list
            otherwise continue to the next iteration
            return the lenght of items in common, which is the number of users
            is common between list1 and list2
     '''
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
        else:
            continue
    return len(common)


def calc_similarity_scores(n):
    ''' loop and create a list of lists that is n x n in size to all zeros that will hold
        number of common friends for each pairing of users.
        loop through the network  of users
            for each friends in each (user)
                find the number of friends in common
                place that value at the position of the same friend and user in the similarity similarity_matrix
        return the similarity matrix '''
    similarity_matrix = []

    for i in range(len(n)):
        new = []
        for e in range(len(n)):
            new.append(0)
        similarity_matrix.append(new)

    for m, v in enumerate(n):
        for user_ids in range(len(n)):
            c = num_in_common_between_lists(n[m], n[user_ids])
            similarity_matrix[m][user_ids] = c
    return similarity_matrix


def recommend(user_id, network, similarity_matrix):

    ''' Find the similarity list of the userid
    find the netwrok list of the userid
    set the user_id in the similar list to zero(to account for itself)
    loop throught the network list
        for each FRIEND(i) in the userid network set it equal to zero in the similar list
    find the max in the mutable list similar_lst
    find the index of that maximum number and return it'''
    similar_lst = similarity_matrix[user_id]
    network_lst = network[user_id]
    similar_lst[user_id] = 0
    for i in network_lst:
        similar_lst[i] = 0
    large = max(similar_lst)
    position = similar_lst.index(large)
    return position


def main():
    # by convention "main" doesn't need a docstring
    while True:
        print("Facebook friend recommendation.\n")
        fp = open_file()
        network = read_file(fp)

        while True:
            try:
                while True:
                    user_id = input("\nEnter an integer in the range 0 to {}:".format(len(network)-1))
                    user_id = int(user_id)
                    if user_id in range(len(network)):
                        break
                    else:
                        print("\nError: input must be an int between 0 and {}".format(len(network) - 1))
                        continue
            except:
                print("\nError: input must be an int between 0 and {}".format(len(network)-1))
                continue
            similarity_matrix = calc_similarity_scores(network)
            index = recommend(user_id, network, similarity_matrix)
            print("\nThe suggested friend for {} is {}".format(user_id, index))
            choice = input("\nDo you want to continue (yes/no)? ").lower()
            if choice == 'yes':
                continue
            else:
                break
        break




if __name__ == "__main__":
    main()

