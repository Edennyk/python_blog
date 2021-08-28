
class Post:
  """
  board class 
  param id 
  param title
  param content
  param view_count
  """
 
  def __init__(self, id , title, content, view_count):
    self.id = id
    self.title = title
    self.content = content
    self.view_count = view_count
  
  def set_post(self, id , title, content, view_count):
    self.id = id
    self.title = title
    self.content = content
    self.view_count = view_count
  
  def add_view_count(self):
    self.view_count += 1
  
  def get_id(self):
    return self.id
  
  def get_title(self):
    return self.title
  
  def get_cotent(self):
    return self.content
    
  def get_view_count(self):
    return self.view_count

# if __name__ == "__main__":
#   post = Post(1, "Test", "This is a Test", 0)
#   post.set_post(1, "Test2", "This is a Test2", 0)
#   post.add_view_count()
#   print(f"{post.get_id()} {post.get_title()} {post.get_cotent()} {post.get_view_count()}")