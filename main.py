import os
import csv
from post import Post

file_path = "./data.csv"

# for save post 
post_list = []

# data.csv file ie exist
if os.path.exists(file_path): # True
  # file loading
  print("file loading....")
  f = open(file_path, "r")
  reader = csv.reader(f)
  
  for data in reader:
    #print(data)
    # create post instance
    post = Post(int(data[0]), data[1], data[2], int(data[3]))
    post_list.append(post)

else: # false
  # create file
  f = open(file_path, "w", newline="")
  f.close()

# create a post (wirte post)
def write_post():
  """ write post method"""
  print("\n\n - write post -")
  title = input("Write a Title\n>>>")
  content = input ("Write a content\n>>>")
  # number of post
  id = post_list[-1].get_id() + 1
  post = Post(id , title , content , 0)
  post_list.append(post)
  print(" # Success ")

# lists of post
def list_post():
  print("\n\n - lists of Post - ")

  id_list =[]

  for post in post_list:
      print("ID:", post.get_id())
      print("Title:", post.get_title())
      print("Views:", post.get_view_count())
      print("")
      id_list.append(post.get_id()) # store id in id_list
  

  while True: 
    print(" Please select number of id (back to menu: -1)")
    try:
      id = int(input(">>>"))
      if id in id_list:
        detail_post(id) # 사용자가 입력한 id 도 같이 넣어 줌
        break
      elif id == -1:
        break
      else:
        print("does not exist id")
    except ValueError:
      print("only number is valid")

# detail of post
def detail_post(id):
    print("\n\n - Detail Page -")

    for post in post_list:
      if post.get_id() == id: # id is correct
        # add count
        post.add_view_count() 
        # detail page output
        print("ID:", post.get_id())
        print("Title:", post.get_title())
        print("Content:", post.get_cotent())
        print("View:", post.get_view_count())
        target_post = post 
    
    # sub menu
    while True:
      print("1. Edit / 2. Delete (back to menu: -1)")
      try:
        choice = int(input(">>>"))
        if choice == 1:
          update_post(target_post)
          break
        elif choice == 2:
          delete_post(target_post)
          break
        elif choice == -1:
          break
        else:
          print("wrong number")
      except ValueError:
        print("only number is valid")

# update post method
def update_post(target_post):
  print("\n\n - Update post -")
  title = input("Write a title\n\>>")
  content = input("Write a content\n>>")
  target_post.set_post(target_post.id, title, content, target_post.view_count)
  print("# Update success")

# delete post method
def delete_post(target_post):
  post_list.remove(target_post)
  print("# Delete success")


# save post method
def save():
  file = open(file_path,"w", newline="")
  writer = csv.writer(file)
  for post in post_list:
    # 이렇게 한줄씩 row를 만들어서 csv 파일에 저장
    row =[post.get_id(), post.get_title(), post.get_cotent(), post.get_view_count()]
    writer.writerow(row)
  file.close()
  print(" # Save success")
  print(" # Bye ~")

  
# Main Menu
while True:
  print("\n\n * Eden Blog *")
  print(" - Select the Menu number -")
  print("1. Write Post")
  print("2. Post List")
  print("3. Exit")
  
  try:
    choice = int(input(">>>")) 
  except ValueError: # if put not a number - error
    print("only number is valid")
  else:
    if choice == 1:
       write_post()
    elif choice == 2:
       list_post()
    elif choice == 3:
       save()
       break