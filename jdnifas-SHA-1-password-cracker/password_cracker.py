import hashlib

def crack_sha1_hash(hash, use_salts = False):
  passwords_arr = []
  read_and_add_to_arr("top-10000-passwords.txt", passwords_arr)
  
  if use_salts:
    top_salt_passwords = {}
    top_salts = []
    read_and_add_to_arr("known-salts.txt", top_salts)
    for bsalt in top_salts:
      for bpassword in passwords_arr:
        prepended = hashlib.sha1(bsalt + bpassword).hexdigest()
        appended = hashlib.sha1(bpassword + bsalt).hexdigest()
        top_salt_passwords[prepended] = bpassword.decode("utf-8")
        top_salt_passwords[appended] = bpassword.decode("utf-8")
    if hash in top_salt_passwords:
      return top_salt_passwords[hash]
      
  else:
    top_10000_passwords = {}
    hash_arr_add_to_dict(passwords_arr, top_10000_passwords)
    if hash in top_10000_passwords:
      return top_10000_passwords[hash]

  return "PASSWORD NOT IN DATABASE"


def read_and_add_to_arr(file_name, arr):
  with open(file_name, "rb") as f:
      line = f.readline().strip()
      while line:
        arr.append(line)
        line = f.readline().strip()

  
def hash_arr_add_to_dict(arr, dict):
  for item in arr:
    hash_line = hashlib.sha1(item).hexdigest()
    dict[hash_line] = item.decode("utf-8")
    