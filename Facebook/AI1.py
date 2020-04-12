import pandas
from sklearn.model_selection import train_test_split
import random
from tkinter import *
pd=Tk()
pd.title("Music Recommended System")
n=int(input("Enter the user number"))

song_list_1 = pandas.read_table(#"Directory of the "Users listen count" Data File should be given")
song_list_1.columns = ['user_id', 'song_id', 'listen_count']
song_list_2 =  pandas.read_csv(#"Directory of the "song_data" Data File should be given")
song_mix = pandas.merge(song_list_1, song_list_2.drop_duplicates(['song_id']), on="song_id", how="left")
song_mix.head()

print("------------------------------------------------------")
users = song_mix['user_id'].unique()
print("Whole Users: %d" % len(users)) 
songs = song_mix['song'].unique()
print("Whole Songs: %d" % len(songs))
print("--------------------------------------------------------------------------------")

Old_data, New_data = train_test_split(song_mix, test_size = 0.20, random_state=0)

New_users = New_data['user_id'].unique()
print("New Trained Users: %d" % len(New_users)) 
New_songs = New_data['song'].unique()
print("New Trained Songs: %d" % len(New_songs))
print("--------------------------------------------------------------------------------")
class song_recommender():
    def __init__(self):
        self.New_data = None
        self.user_id = None
        self.item_id = None
        
    #Get unique items corresponding to a given user
    def get_user_items_New_data(self, user):
        user_data = self.New_data[self.New_data[self.user_id] == user]
        user_items = list(user_data[self.item_id].unique())
        
        return user_items
        
    #Get unique users for a given item
    def get_item_users_New_data(self, item):
        item_data = self.New_data[self.New_data[self.item_id] == item]
        item_users = set(item_data[self.user_id].unique())
            
        return item_users
        
    #Get unique items in the training data
    def get_all_items_new_data(self):
        all_items = list(self.New_data[self.item_id].unique())
            
        return all_items
    def create(self, New_data, user_id, item_id):
        self.New_data = New_data
        self.user_id = user_id
        self.item_id = item_id

    #make recommendations
    def recommend(self, user):
        
        # Gets all unique songs for this user
        
        user_songs = self.get_user_items_New_data(user)    
            
        print("No. of unique songs for the user: %d" % len(user_songs))
        
        
        # Gets all unique items (songs) in the training data
        
        all_songs = self.get_all_items_new_data()
        
        print("No. of unique songs in the training set: %d" % len(all_songs))

    def users_for_the_given_item(self,item):
        
        # Gets all unique users (songs) in the training data
        for i in item:
            unique_users = self.get_item_users_New_data(i)

            l=Label(pd,text=i+" : %d People Listen Daily"%len(unique_users))
            l.pack(side=BOTTOM)
        

is_model = song_recommender()
is_model.create(New_data, 'user_id', 'song')

#Print the songs for the user in New Data

user_id = New_users[n]
user_items = is_model.get_user_items_New_data(user_id)
print("User-id: %s:" % user_id)

print("--------------------------------------------------------------------------------")


#Using Tkinter Function for Displaying the User's Songs

v=Label(pd,text="Recommended Songs for the given user",font="Helvetica 16 bold italic")
v.pack()
q=Label(pd,text="------------------------------------------------------------------------------------")
q.pack()
scrollbar = Scrollbar(pd) 
scrollbar.pack( side = RIGHT, fill = Y )
list1=Listbox(pd,width=60,yscrollcommand=scrollbar.set)
for i in range(len(user_items)):
    list1.insert(END,user_items[i])
list1.pack()
scrollbar.config(command=list1.yview)
q=Label(pd,text="------------------------------------------------------------------------------------")
q.pack()
pop=[]
for i in range(0,5):
    pop.append(random.choice(New_songs))

u=Label(pd,text="Know More Songs",font="Helvetica 13 bold italic")
u.pack()
q=Label(pd,text="------------------------------------------------------------------------------------")
q.pack()
is_model.users_for_the_given_item(pop)


#Recommend Songs for the user using Personal Songs played by the user

is_model.recommend(user_id)
print("--------------------------------------------------------------------------------")


